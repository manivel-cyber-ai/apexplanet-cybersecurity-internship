# Task 3 — Web Application Security
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 25–36

![Task](https://img.shields.io/badge/Task-3%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%2025--36-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Burp%20Suite%20%7C%20DVWA%20%7C%20sqlmap%20%7C%20Nikto%20%7C%20curl-red)

---

## 🎯 Objective

Identify and exploit OWASP Top 10 vulnerabilities in a controlled lab environment using DVWA on Metasploitable2.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task3-notes.md` | Detailed notes covering the main Task 3 topics |
| `task3-cheatsheet.md` | Quick reference for SQL injection, XSS, CSRF, LFI, and Burp Suite |
| `csrf-demo.html` | CSRF attack demo page for educational use |
| `screenshots/` | Evidence screenshots from the attack demonstrations |
| `README.md` | This file |

---

## 🧪 Lab Setup

| Component | Details |
|-----------|---------|
| **Attacker OS** | Kali Linux |
| **Target VM** | Metasploitable2 |
| **Target IP** | 192.168.56.101 |
| **Web App** | DVWA at `http://192.168.56.101/dvwa` |
| **DVWA Security** | Low (for demonstration) |
| **Proxy Tool** | Burp Suite Community Edition |

---

## ✅ Vulnerabilities Demonstrated

### 1. SQL Injection (SQLi)
- Tested input fields with `'` and confirmed vulnerability through error output
- Extracted database names, table names, and column names
- Dumped usernames and password hashes from the `users` table using UNION-based SQLi
- Demonstrated prevention using prepared statements

### 2. Cross-Site Scripting (XSS)
- **Reflected XSS** — injected a script via a URL parameter
- **Stored XSS** — persisted a malicious script through a message field
- Demonstrated cookie harvesting using a Python HTTP server
- Mitigation: content security policy and proper input encoding

### 3. Cross-Site Request Forgery (CSRF)
- Created `csrf-demo.html` as a hidden form that auto-submits to change an admin password
- Demonstrated the attack with the victim already logged into DVWA in another tab
- Prevention: CSRF tokens and SameSite cookie attributes

### 4. File Inclusion Attacks
- **LFI** — read `/etc/passwd` through a URL parameter
- **RFI** — host a PHP web shell on Kali and include it through the target application
- Executed OS commands such as `id`, `whoami`, and `cat /etc/passwd`
- Prevention: input whitelisting and `allow_url_include=Off`

### 5. Burp Suite Advanced
- Intercepted and modified login requests via proxy
- Used Repeater to manually test different parameter values
- Used Intruder for password fuzzing with a wordlist
- Demonstrated Decoder for Base64 and URL encoding

### 6. Web Security Headers
- Analyzed response headers using `curl -I`
- Added security headers to the Apache configuration, including CSP and HSTS settings

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Burp Suite | HTTP proxy, request interception, and fuzzing |
| DVWA | Vulnerable target web application |
| sqlmap | Automated SQL injection testing |
| Nikto | Web server vulnerability scanning |
| curl | HTTP request analysis and header checking |
| Python HTTP Server | Hosting files for demonstration purposes |
| Firefox | Browser with Burp proxy configured |

---

## 🔍 Key Findings

| Vulnerability | Severity | Impact |
|--------------|----------|--------|
| SQL Injection | 🔴 Critical | Full database access and credential exposure |
| Stored XSS | 🔴 Critical | Cookie theft and session hijacking |
| Reflected XSS | 🟠 High | Phishing and credential theft |
| CSRF | 🟠 High | Unauthorized actions as the victim |
| LFI | 🟠 High | Sensitive file disclosure |
| RFI | 🔴 Critical | Remote code execution |
| Missing Security Headers | 🟡 Medium | Clickjacking and MIME sniffing risk |

---

## 📦 Deliverables

- [x] SQL injection demonstration with extracted credentials
- [x] Reflected and stored XSS demonstrations
- [x] CSRF password change attack via `csrf-demo.html`
- [x] LFI and RFI demonstrations
- [x] Burp Suite interception and fuzzing activity
- [x] Security header analysis and mitigation notes
- [x] GitHub repository with attack scenarios and mitigation notes
- [x] Short demo video on LinkedIn

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](https://www.linkedin.com/posts/mr-manivel-r_cybersecurity-ethicalhacking-websecurity-activity-7488228100615323649-bQsO?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGDJA9sBzSi23edH7UWChoU_mcEMAARlJJ8)
- 📁 **Main Repo:** [apexplanet-cybersecurity-internship](https://github.com/manivel-cyber-ai/apexplanet-cybersecurity-internship)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)

---

> ⚠️ All attacks were performed exclusively in an isolated lab environment for educational purposes.
> Performing these attacks on real systems without authorization is illegal under cybercrime laws.

*Manivel R | ApexPlanet Internship 2026 | Anna University*

