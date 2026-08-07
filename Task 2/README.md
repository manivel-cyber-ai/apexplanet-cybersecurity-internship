# Task 2 — Network Security & Scanning
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 13–24

![Task](https://img.shields.io/badge/Task-2%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%2013--24-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Nmap%20%7C%20Wireshark%20%7C%20OpenVAS%20%7C%20hping3%20%7C%20iptables-red)

---

## 🎯 Objective

Learn reconnaissance techniques, network scanning, vulnerability assessment, packet analysis, and basic firewall configuration in a controlled lab environment.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task2-notes.md` | Detailed notes covering the major Task 2 topics |
| `task2-cheatsheet.md` | Quick reference for Nmap, Wireshark, and iptables |
| `task2-nmap-report.txt` | Full Nmap scan output against Metasploitable2 |
| `open-vas-report.pdf` | OpenVAS vulnerability assessment report |
| `ip-tables.png` | Screenshot showing example firewall rule output |
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
**Passive Recon** — no direct contact with the target
- `whois` — domain registration details
- `nslookup` and `dig` — DNS resolution and record lookup
- Google dorking — finding exposed files and pages
- Shodan — discovering internet-exposed services

**Active Recon** — direct interaction with the target
- Ping sweep with Nmap
- Banner grabbing with Netcat on ports 22 and 80

### 2. Port & Service Scanning
- TCP SYN scan (`-sS`) and UDP scan (`-sU`)
- Service version detection (`-sV`)
- OS detection (`-O`)
- Aggressive scan (`-A`) with results saved to a text report
- Identified open ports such as FTP, SSH, Telnet, HTTP, and MySQL

### 3. Vulnerability Scanning
- Set up OpenVAS (GVM) on Kali Linux
- Scanned Metasploitable2 as the target
- Reviewed the report for severity-based findings

### 4. Packet Analysis with Wireshark
- Captured HTTP, FTP, and DNS traffic
- Demonstrated FTP credential exposure in plaintext
- Simulated SYN flood traffic using hping3
- Examined traffic using filters such as `tcp.flags.syn == 1`

### 5. Firewall Basics with iptables
- Created rules to allow or deny specific ports
- Blocked port 22 (SSH) and demonstrated the resulting connection failure
- Reset rules using `iptables -F`

---

## 🛠️ Tools Used

| Tool | Purpose | Key Command |
|------|---------|-------------|
| Nmap | Port and service scanning | `nmap -A -oN report.txt <target>` |
| Wireshark | Packet capture and analysis | FTP filter, SYN flood filter |
| OpenVAS | Vulnerability scanning | Web UI at `127.0.0.1:9392` |
| hping3 | SYN flood simulation | `hping3 -S --flood -p 80 <target>` |
| iptables | Firewall rule management | `iptables -A INPUT -p tcp --dport 22 -j DROP` |
| Netcat | Banner grabbing | `nc <target> 22` |
| whois / dig | Passive reconnaissance | `dig google.com`, `whois domain.com` |

---

## 🔍 Key Findings

### Nmap Scan Summary
```text
Target: 192.168.56.101 (Metasploitable2)
Open ports found:
  21/tcp  - FTP     (vsftpd 2.3.4)
  22/tcp  - SSH     (OpenSSH 4.7p1)
  23/tcp  - Telnet
  80/tcp  - HTTP    (Apache 2.2.8)
  3306/tcp - MySQL  (5.0.51a)
OS detected: Linux 2.6.x
```

### Wireshark FTP Finding
> FTP transmitted credentials in plaintext, which highlights the importance of using SFTP or FTPS instead.

---

## 📦 Deliverables

- [x] Nmap scan report in `task2-nmap-report.txt`
- [x] OpenVAS vulnerability report in `open-vas-report.pdf`
- [x] Wireshark FTP capture evidence
- [x] SYN flood simulation evidence
- [x] iptables firewall rule evidence
- [x] GitHub repository with scan analysis
- [x] Short demo video on LinkedIn

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](#)
- 📁 **Main Repo:** [apexplanet-cybersecurity-internship](https://github.com/manivel-cyber-ai/apexplanet-cybersecurity-internship)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)

---

> ⚠️ All activities were performed in an isolated lab environment for educational purposes only. Unauthorized scanning of real systems without permission is illegal.

*Manivel R | ApexPlanet Internship 2026 | Anna University*

