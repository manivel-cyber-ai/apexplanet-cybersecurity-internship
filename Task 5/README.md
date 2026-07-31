# DVWA Web Application Penetration Test — Capstone Project

**ApexPlanet Cybersecurity & Ethical Hacking Internship — Task 5**
Offer Letter ID: APSPL2640160

## Overview

A controlled-environment penetration test of DVWA (Damn Vulnerable Web Application) across all three built-in security levels (low, medium, high), covering SQL Injection, XSS, CSRF, LFI/RFI, and authentication weaknesses — followed by an incident-response simulation demonstrating detection, containment, and eradication of a live attack.

**Disclaimer:** All testing was performed exclusively against DVWA running in an isolated, host-only virtual lab network under my own control. No external or third-party systems were targeted.

## Repo Structure

```
.
├── README.md
├── report/
│   ├── DVWA_Pentest_Report.docx
│   └── DVWA_Pentest_Report.pdf
├── diagrams/
│   └── network_diagram.svg
├── scripts/
│   └── log_detection.py          # IR log-analysis / signature detection tool
├── evidence/
│   ├── sqli/
│   ├── xss/
│   ├── csrf/
│   ├── file_inclusion/
│   └── incident_response/
├── logs/
│   └── sample_access.log         # captured during exploitation, used for IR demo
└── docs/
    └── procedure.md              # step-by-step methodology followed
```

## Lab Environment

| Role | Machine | IP |
|---|---|---|
| Attacker | Kali Linux | 192.168.56.10 |
| Target | Metasploitable2 / DVWA | 192.168.56.20 |

Network: VirtualBox Host-Only Adapter, `192.168.56.0/24`, no internet egress from target.

## Vulnerabilities Tested

| ID | Vulnerability | Severity |
|---|---|---|
| F-01 | SQL Injection | Critical |
| F-02 | Reflected XSS | High |
| F-03 | Stored XSS | High |
| F-04 | CSRF (password change) | Medium |
| F-05 | Local File Inclusion | Critical |
| F-06 | Remote File Inclusion | Critical |
| F-07 | No account lockout | Low |

Full details, PoC steps, and mitigations: see [`report/DVWA_Pentest_Report.pdf`](./report/DVWA_Pentest_Report.pdf).

## Incident Response Simulation

`scripts/log_detection.py` scans Apache access logs for known attack signatures (SQLi, XSS, LFI/RFI patterns) and flags source IP, timestamp, and severity — used to demonstrate detection → containment (`iptables` block) → eradication (raising DVWA security level) → post-incident reporting.

```bash
python3 scripts/log_detection.py logs/sample_access.log --out findings.csv
```

## Tools Used

Nmap · Nikto · Burp Suite · sqlmap · Hydra · Wireshark · custom Python detection script

## Video Walkthrough

12-minute demonstration: [LinkedIn link — add after upload]

## Author

Manivel R — B.E. CSE (AI & ML), University College of Engineering, BIT Campus, Anna University
[manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io) · [LinkedIn](https://linkedin.com/in/mr-manivel-r)
