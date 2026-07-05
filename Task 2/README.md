# Task 2 — Network Security & Scanning
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 13–24

![Task](https://img.shields.io/badge/Task-2%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%2013--24-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Nmap%20%7C%20Wireshark%20%7C%20OpenVAS%20%7C%20hping3%20%7C%20iptables-red)

---

## 🎯 Objective

Learn reconnaissance techniques, network scanning, vulnerability assessment, packet analysis, and basic firewall configuration against a controlled lab target.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task2-notes.md` | Detailed notes covering all 5 topics of Task 2 |
| `task2-cheatsheet.md` | Quick reference for Nmap, Wireshark, iptables |
| `task2-nmap-report.txt` | Full Nmap scan output against Metasploitable2 |
| `task2-openvas-report.pdf` | OpenVAS vulnerability assessment report |
| `screenshots/` | Evidence screenshots from all activities |
| `README.md` | This file |

---

## 🧪 Lab Setup

| Component | Details |
|-----------|---------|
| **Attacker OS** | Kali Linux |
| **Target VM** | Metasploitable2 |
| **Target IP** | 192.168.56.101 |
| **Network** | Host-Only Adapter (VirtualBox) |

---

## ✅ Topics Covered

### 1. Reconnaissance
**Passive Recon** — no direct contact with target
- `whois` — domain registration details
- `nslookup` / `dig` — DNS resolution and records
- Google Dorking — finding exposed files/pages
- Shodan — discovering internet-exposed services

**Active Recon** — direct interaction with target
- Ping sweep with Nmap
- Banner grabbing with Netcat on ports 22 and 80

### 2. Port & Service Scanning
- TCP SYN scan (`-sS`) and UDP scan (`-sU`)
- Service version detection (`-sV`)
- OS detection (`-O`)
- Aggressive scan (`-A`) with full report saved to file
- Identified open ports: 21/FTP, 22/SSH, 23/Telnet, 80/HTTP, 3306/MySQL and more

### 3. Vulnerability Scanning
- Set up OpenVAS (GVM) on Kali Linux
- Scanned Metasploitable2 as target
- Analyzed vulnerability report by severity:

| Severity | Count |
|----------|-------|
| Critical | |
| High | |
| Medium | |
| Low | |

> *(Update counts after OpenVAS scan)*

### 4. Packet Analysis with Wireshark
- Captured HTTP, FTP, DNS traffic
- Demonstrated FTP plaintext credential capture
- Simulated SYN flood attack using hping3
- Analyzed flood traffic with `tcp.flags.syn == 1` filter

### 5. Firewall Basics with iptables
- Created rules to allow/deny specific ports
- Blocked port 22 (SSH) and demonstrated connection failure
- Reset rules with `iptables -F`

---

## 🛠️ Tools Used

| Tool | Purpose | Key Command |
|------|---------|-------------|
| Nmap | Port & service scanning | `nmap -A -oN report.txt <target>` |
| Wireshark | Packet capture & analysis | FTP filter, SYN flood filter |
| OpenVAS | Vulnerability scanning | Web UI at 127.0.0.1:9392 |
| hping3 | SYN flood simulation | `hping3 -S --flood -p 80 <target>` |
| iptables | Firewall rule management | `iptables -A INPUT -p tcp --dport 22 -j DROP` |
| Netcat | Banner grabbing | `nc <target> 22` |
| whois/dig | Passive reconnaissance | `dig google.com`, `whois domain.com` |

---

## 🔍 Key Findings

### Nmap Scan Summary
```
Target: 192.168.56.101 (Metasploitable2)
Open Ports Found:
  21/tcp  - FTP     (vsftpd 2.3.4)
  22/tcp  - SSH     (OpenSSH 4.7p1)
  23/tcp  - Telnet
  80/tcp  - HTTP    (Apache 2.2.8)
  3306/tcp - MySQL  (5.0.51a)
  ...
OS Detected: Linux 2.6.x
```

### Wireshark FTP Finding
> FTP transmits credentials in **plaintext** — username and password were clearly visible in the packet capture. This demonstrates why FTP should be replaced with SFTP or FTPS.

### OpenVAS Key Vulnerabilities
> *(Add top 3 findings after scan)*

---

## 📦 Deliverables

- [x] Nmap Scan Report (`task2-nmap-report.txt`)
- [x] OpenVAS Vulnerability Report (PDF)
- [x] Wireshark FTP credential capture (screenshot)
- [x] SYN flood simulation (screenshot)
- [x] iptables firewall rules (screenshot)
- [x] GitHub Repo with scan analysis
- [x] 5-min Demo Video on LinkedIn

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](#)
- 📁 **Main Repo:** [apexplanet-cybersecurity-internship](https://github.com/manivel-cyber-ai/apexplanet-cybersecurity-internship)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)

---

> ⚠️ All activities performed in an isolated lab environment for educational purposes only. Unauthorized scanning of real systems without permission is illegal.

*Manivel R | ApexPlanet Internship 2026 | Anna University*

