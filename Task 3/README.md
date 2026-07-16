# Task 3 — Web Application Security
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 25–36

![Task](https://img.shields.io/badge/Task-3%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%2025--36-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Burp%20Suite%20%7C%20DVWA%20%7C%20sqlmap%20%7C%20Nikto%20%7C%20curl-red)

---

## 🎯 Objective

Identify and exploit OWASP Top 10 vulnerabilities in a controlled lab environment using DVWA (Damn Vulnerable Web Application) on Metasploitable2.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task3-notes.md` | Detailed notes covering all 6 topics of Task 3 |
| `task3-cheatsheet.md` | Quick reference for SQLi, XSS, CSRF, LFI, Burp Suite |
| `csrf-demo.html` | CSRF attack demo page (educational use only) |
| `screenshots/` | Evidence screenshots from all attack demonstrations |
| `README.md` | This file |

---

## 🧪 Lab Setup

| Component | Details |
|-----------|---------|
| **Attacker OS** | Kali Linux |
| **Target VM** | Metasploitable2 |
| **Target IP** | 192.168.56.101 |
| **Web App** | DVWA at http://192.168.56.101/dvwa |
| **DVWA Security** | Low (for demonstration) |
| **Proxy Tool** | Burp Suite Community Edition |

---

## ✅ Vulnerabilities Demonstrated

### 1. SQL Injection (SQLi)
- Tested input fields with `'` — confirmed vulnerability via error
- Extracted database name, table names, column names
- Dumped username and password hashes from `users` table using UNION-based SQLi
- Demonstrated prevention using Prepared Statements

### 2. Cross-Site Scripting (XSS)
- **Reflected XSS** — injected `<script>alert(document.cookie)</script>` via URL parameter
- **Stored XSS** — persisted malicious script in database via message field
- Demonstrated cookie harvesting using Python HTTP server
- Mitigation: Content Security Policy (CSP) header + input encoding

### 3. Cross-Site Request Forgery (CSRF)
- Created `csrf-demo.html` — hidden form auto-submits to change admin password
- Demonstrated attack with victim logged into DVWA in another tab
- Password successfully changed without user interaction
- Prevention: CSRF tokens, SameSite cookie attribute

### 4. File Inclusion Attacks
- **LFI** — Read `/etc/passwd` via `?page=../../../../etc/passwd`
- **RFI** — Hosted PHP webshell on Kali, included via URL parameter
- Executed OS commands (`id`, `whoami`, `cat /etc/passwd`) through RFI shell
- Prevention: Input whitelist, `allow_url_include=Off` in php.ini

### 5. Burp Suite Advanced
- Intercepted and modified login requests via proxy
- Used Repeater to manually test different parameter values
- Used Intruder for password fuzzing with rockyou.txt wordlist
- Demonstrated Decoder for Base64/URL encoding/decoding

### 6. Web Security Headers
- Analyzed headers using `curl -I` and securityheaders.com
- Added security headers to Apache configuration:
  - `X-Frame-Options: DENY`
  - `X-XSS-Protection: 1; mode=block`
  - `X-Content-Type-Options: nosniff`
  - `Content-Security-Policy: default-src 'self'`
  - `Strict-Transport-Security: max-age=31536000`

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Burp Suite | HTTP proxy, request interception, fuzzing |
| DVWA | Target vulnerable web application |
| sqlmap | Automated SQL injection testing |
| Nikto | Web server vulnerability scanner |
| curl | HTTP request analysis and header checking |
| Python HTTP Server | Hosting malicious files for RFI/XSS demo |
| Firefox | Browser with Burp proxy configured |

---

## 🔍 Key Findings

| Vulnerability | Severity | Impact |
|--------------|----------|--------|
| SQL Injection | 🔴 Critical | Full database access, credential dump |
| Stored XSS | 🔴 Critical | Cookie theft, session hijacking |
| Reflected XSS | 🟠 High | Phishing, credential theft |
| CSRF | 🟠 High | Unauthorized actions as victim |
| LFI | 🟠 High | Sensitive file disclosure |
| RFI | 🔴 Critical | Remote code execution |
| Missing Security Headers | 🟡 Medium | Clickjacking, MIME sniffing |

---

## 📦 Deliverables

- [x] SQL Injection — credentials extracted from DVWA database
- [x] XSS — Reflected and Stored demonstrated with cookie theft
- [x] CSRF — Password change attack via `csrf-demo.html`
- [x] LFI — `/etc/passwd` read via URL parameter
- [x] RFI — Remote PHP shell executed OS commands
- [x] Burp Suite — Request intercepted + Intruder fuzzing done
- [x] Security Headers — Analyzed and added to Apache config
- [x] GitHub Repo with attack scenarios + mitigation notes
- [x] 8-min Video Demo on LinkedIn

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](#)
- 📁 **Main Repo:** [apexplanet-cybersecurity-internship](https://github.com/manivel-cyber-ai/apexplanet-cybersecurity-internship)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)

---

> ⚠️ All attacks performed exclusively in an isolated lab environment for educational purposes.
> Performing these attacks on real systems without authorization is illegal under the IT Act and cybercrime laws.

*Manivel R | ApexPlanet Internship 2026 | Anna University*

