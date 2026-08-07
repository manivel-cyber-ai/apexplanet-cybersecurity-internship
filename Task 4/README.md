# Task 4 — Exploitation & System Security
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 37–48

![Task](https://img.shields.io/badge/Task-4%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%2037--48-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Metasploit%20%7C%20Hydra%20%7C%20John%20%7C%20msfvenom%20%7C%20SET-red)

---

## 🎯 Objective

Learn the full penetration testing workflow and responsibly exploit vulnerabilities in a controlled lab environment, covering exploitation, post-exploitation, password attacks, social engineering simulation, malware basics, and system hardening.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task4-notes.md` | Detailed notes covering the main Task 4 topics |
| `task4-cheatsheet.md` | Quick reference for Metasploit, Hydra, John, and msfvenom |
| `malware-analysis/` | Folder containing malware analysis notes and related material |
| `screenshots/` | Evidence screenshots from the exercises |
| `README.md` | This file |

---

## 🧪 Lab Setup

| Component | Details |
|-----------|---------|
| **Attacker OS** | Kali Linux |
| **Target VM** | Metasploitable2 |
| **Target IP** | 192.168.93.129 |
| **Attacker IP** | 192.168.93.128 |
| **Network** | NAT Network (VirtualBox) |

---

## ✅ Activities Completed

### 1. Penetration Testing Methodology
- Followed the standard pentest workflow: reconnaissance → scanning → exploitation → post-exploitation → reporting
- Documented each step with timestamps and screenshots
- Performed an initial Nmap scan using `nmap -sV -O 192.168.93.129`

### 2. Exploitation with Metasploit

#### vsftpd 2.3.4 Backdoor Exploit
```text
Module  : exploit/unix/ftp/vsftpd_234_backdoor
Target  : 192.168.93.129 (port 21)
Result  : Root shell obtained
```

#### Samba Usermap Script Exploit
```text
Module  : exploit/multi/samba/usermap_script
Target  : 192.168.93.129 (port 445)
Result  : Root shell obtained
```

#### Post-Exploitation Commands Run
- `sysinfo` — gathered OS and hardware information
- `cat /etc/shadow` — dumped password hashes
- `netstat -tulpn` — listed open ports
- `ps aux` — listed running processes
- `find / -perm -4000` — found SUID binaries

### 3. Password Attacks

#### Hydra — SSH Brute Force
```bash
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt -t 4 ssh://192.168.93.129
# Result: msfadmin:msfadmin found
```

#### John the Ripper — Hash Cracking
```bash
unshadow /etc/passwd /etc/shadow > combined.txt
john combined.txt --wordlist=/usr/share/wordlists/rockyou.txt
# Result: Multiple passwords cracked
```

### 4. Social Engineering Simulation
- Used SET to clone a login page
- Created phishing awareness training materials
- Demonstrated common red flags in phishing attempts

### 5. Malware Basics
- Performed static analysis using `file`, `strings`, `readelf`, and hash verification
- Performed dynamic analysis using `strace`, `ltrace`, and network monitoring
- Reviewed the sample in a sandbox and documented the observed behavior

### 6. System Hardening
- Enabled UFW with allow and deny rules
- Blocked Telnet (port 23) and FTP (port 21)
- Configured SSH hardening by disabling root login
- Identified SUID binaries using `find / -perm -4000`
- Applied patches with `apt update && apt upgrade`

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Metasploit (msfconsole) | Exploitation framework |
| msfvenom | Payload generation |
| Hydra | Online brute force attacks |
| John the Ripper | Offline hash cracking |
| SET | Social engineering simulation |
| UFW / iptables | Firewall configuration |
| strace / ltrace | Malware dynamic analysis |
| Nmap | Pre-exploitation scanning |

---

## 🔍 Key Findings

| Vulnerability | CVE | Severity | Result |
|--------------|-----|----------|--------|
| vsftpd 2.3.4 backdoor | CVE-2011-2523 | 🔴 Critical | Root shell |
| Samba Usermap script | CVE-2007-2447 | 🔴 Critical | Root shell |
| Weak SSH credentials | — | 🟠 High | SSH access via brute force |
| Password reuse | — | 🟠 High | Multiple accounts cracked |

---

## 📦 Deliverables

- [x] Penetration testing report with screenshots
- [x] Metasploit exploitation using the vsftpd and Samba exploits
- [x] Post-exploitation activity including hash dumps and process listing
- [x] Hydra SSH brute force activity
- [x] John the Ripper hash cracking activity
- [x] Social engineering simulation materials
- [x] Malware static and dynamic analysis notes
- [x] System hardening steps and evidence
- [x] GitHub repository with exploitation steps and mitigations
- [x] Short demo video on LinkedIn

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](https://www.linkedin.com/posts/mr-manivel-r_cybersecurity-ethicalhacking-penetrationtesting-ugcPost-7488652847006306304-2vMU/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGDJA9sBzSi23edH7UWChoU_mcEMAARlJJ8)
- 📁 **Main Repo:** [apexplanet-cybersecurity-internship](https://github.com/manivel-cyber-ai/apexplanet-cybersecurity-internship)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)

---

> ⚠️ All exploitation activities were performed exclusively in an isolated lab environment (Metasploitable2) for educational purposes only.
> Unauthorized access to real systems is illegal under cybercrime laws.
> This internship follows responsible disclosure and ethical hacking principles.

*Manivel R | ApexPlanet Internship 2026 | Anna University*

