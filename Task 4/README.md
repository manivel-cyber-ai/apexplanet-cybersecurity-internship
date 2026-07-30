# Task 4 — Exploitation & System Security
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 37–48

![Task](https://img.shields.io/badge/Task-4%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%2037--48-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Metasploit%20%7C%20Hydra%20%7C%20John%20%7C%20msfvenom%20%7C%20SET-red)

---

## 🎯 Objective

Learn the full penetration testing workflow and responsibly exploit vulnerabilities in a controlled lab environment — covering exploitation, post-exploitation, password attacks, social engineering simulation, malware basics, and system hardening.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task4-notes.md` | Detailed notes covering all 6 topics of Task 4 |
| `task4-cheatsheet.md` | Quick reference for Metasploit, Hydra, John, msfvenom |
| `screenshots/` | Evidence screenshots from all activities |
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
- Followed full 5-phase pentest workflow:
  `Recon → Scanning → Exploitation → Post-Exploitation → Reporting`
- Documented every step with timestamps and screenshots
- Pre-scan with Nmap: `nmap -sV -O 192.168.93.129`

### 2. Exploitation with Metasploit

#### vsftpd 2.3.4 Backdoor Exploit
```
Module  : exploit/unix/ftp/vsftpd_234_backdoor
Target  : 192.168.93.129 (port 21)
Result  : Root shell obtained
```

#### Samba Usermap Script Exploit
```
Module  : exploit/multi/samba/usermap_script
Target  : 192.168.93.129 (port 445)
Result  : Root shell obtained
```

#### Post-Exploitation Commands Run
- `sysinfo` — gathered OS and hardware info
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
- Used SET (Social Engineering Toolkit) to clone a login page
- Created phishing awareness training materials
- Demonstrated red flags for identifying phishing attempts

### 5. Malware Basics
- Performed static analysis: `file`, `strings`, `readelf`, hash verification
- Performed dynamic analysis: `strace`, `ltrace`, network traffic monitoring
- Analyzed sample in sandbox — noted system calls and network connections

### 6. System Hardening
- Enabled UFW firewall with allow/deny rules
- Blocked Telnet (port 23) and FTP (port 21)
- Configured SSH hardening: `PermitRootLogin no`
- Found SUID binaries using `find / -perm -4000`
- Applied system patches: `apt update && apt upgrade`

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
| vsftpd 2.3.4 Backdoor | CVE-2011-2523 | 🔴 Critical | Root shell |
| Samba Usermap Script | CVE-2007-2447 | 🔴 Critical | Root shell |
| Weak SSH credentials | — | 🟠 High | SSH access via brute force |
| Password reuse | — | 🟠 High | Multiple accounts cracked |

---

## 📦 Deliverables

- [x] Penetration Testing Report with screenshots
- [x] Metasploit exploitation — vsftpd + Samba exploits
- [x] Post-exploitation — sysinfo, hashdump, process listing
- [x] Hydra SSH brute force — credentials found
- [x] John the Ripper — hashes cracked
- [x] Social Engineering simulation page (SET)
- [x] Malware static + dynamic analysis
- [x] System hardening — UFW, SSH config, SUID audit
- [x] GitHub Repo with exploitation steps + mitigations
- [x] 10-min Demo Video on LinkedIn

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](https://www.linkedin.com/posts/mr-manivel-r_cybersecurity-ethicalhacking-penetrationtesting-ugcPost-7488652847006306304-2vMU/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGDJA9sBzSi23edH7UWChoU_mcEMAARlJJ8)
- 📁 **Main Repo:** [apexplanet-cybersecurity-internship](https://github.com/manivel-cyber-ai/apexplanet-cybersecurity-internship)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)

---

> ⚠️ All exploitation activities performed exclusively in an isolated lab environment (Metasploitable2) for educational purposes only.
> Unauthorized access to real systems is illegal under the IT Act and cybercrime laws.
> This internship follows responsible disclosure and ethical hacking principles.

*Manivel R | ApexPlanet Internship 2026 | Anna University*

