#!/usr/bin/env python3
"""
log_detection.py — Task 5 Incident Response: Log-based attack detection

Scans an Apache access log (or MySQL general query log) for signatures
of SQLi, XSS, and LFI/RFI attacks, and reports matches with timestamp,
source IP, and matched pattern so you can build the IR timeline.

Usage:
    python3 log_detection.py /var/log/apache2/access.log
    python3 log_detection.py /var/log/apache2/access.log --out findings.csv
"""

import argparse
import csv
import re
import sys
from collections import Counter

# Detection signatures: (label, regex, severity)
SIGNATURES = [
    ("SQL Injection - UNION",        r"UNION(\s|%20)+SELECT", "Critical"),
    ("SQL Injection - Boolean",      r"(\bOR\b|\bAND\b)\s*['\"]?\d+['\"]?\s*=\s*['\"]?\d+", "Critical"),
    ("SQL Injection - Comment",      r"(--|#|/\*)", "Medium"),
    ("SQL Injection - Quote probe",  r"(%27|'){1}.*?(OR|AND|SELECT|UNION)", "High"),
    ("XSS - script tag",             r"<script[^>]*>", "High"),
    ("XSS - event handler",          r"on(error|load|mouseover|click)\s*=", "Medium"),
    ("XSS - javascript URI",         r"javascript:", "Medium"),
    ("LFI - path traversal",         r"(\.\./|%2e%2e%2f){2,}", "Critical"),
    ("LFI - sensitive file",         r"(etc/passwd|boot\.ini|win\.ini)", "Critical"),
    ("RFI - remote include",         r"(https?|ftp)://.*\.(php|txt)", "Critical"),
    ("Command Injection",            r"(;|\||&&)\s*(cat|ls|whoami|id|wget|curl)\b", "Critical"),
]

# Apache combined log format:
# IP - - [timestamp] "METHOD /path HTTP/1.1" status size "referrer" "UA"
LOG_LINE_RE = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\S+)'
)

COMPILED_SIGS = [(label, re.compile(pattern, re.IGNORECASE), sev) for label, pattern, sev in SIGNATURES]


def scan_file(path):
    findings = []
    with open(path, "r", errors="ignore") as f:
        for line_num, line in enumerate(f, start=1):
            m = LOG_LINE_RE.search(line)
            ip = m.group("ip") if m else "unknown"
            ts = m.group("time") if m else "unknown"
            target_text = m.group("request") if m else line

            for label, pattern, severity in COMPILED_SIGS:
                match = pattern.search(target_text)
                if match:
                    findings.append({
                        "line_number": line_num,
                        "timestamp": ts,
                        "source_ip": ip,
                        "signature": label,
                        "severity": severity,
                        "matched_text": match.group(0)[:80],
                        "raw_line": line.strip()[:200],
                    })
    return findings


def print_report(findings):
    if not findings:
        print("No attack signatures detected.")
        return

    print(f"\n{'='*70}\nDetected {len(findings)} suspicious log entries\n{'='*70}\n")
    for f in findings:
        print(f"[{f['severity']:>8}] line {f['line_number']:>5} | {f['timestamp']} | "
              f"src={f['source_ip']} | {f['signature']} | matched: {f['matched_text']!r}")

    print(f"\n{'-'*70}\nSummary by signature type:")
    counts = Counter(f["signature"] for f in findings)
    for sig, count in counts.most_common():
        print(f"  {sig:30s} {count}")

    print(f"\nSummary by source IP (top offenders):")
    ip_counts = Counter(f["source_ip"] for f in findings)
    for ip, count in ip_counts.most_common(5):
        print(f"  {ip:20s} {count} hits  <-- candidate for containment (iptables DROP)")


def write_csv(findings, out_path):
    if not findings:
        return
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=findings[0].keys())
        writer.writeheader()
        writer.writerows(findings)
    print(f"\nFindings written to {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Detect attack signatures in web server logs (Task 5 IR simulation).")
    parser.add_argument("logfile", help="Path to Apache access log or similar")
    parser.add_argument("--out", help="Optional path to write findings as CSV", default=None)
    args = parser.parse_args()

    try:
        findings = scan_file(args.logfile)
    except FileNotFoundError:
        print(f"Error: log file not found: {args.logfile}", file=sys.stderr)
        sys.exit(1)

    print_report(findings)
    if args.out:
        write_csv(findings, args.out)


if __name__ == "__main__":
    main()
