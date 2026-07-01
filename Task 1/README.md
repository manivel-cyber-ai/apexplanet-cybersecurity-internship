# Task 1 — Foundation & Environment Setup
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 1–12

![Task](https://img.shields.io/badge/Task-1%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%201--12-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Kali%20%7C%20Nmap%20%7C%20Wireshark%20%7C%20Burp%20Suite%20%7C%20Netcat-red)

---

## 🎯 Objective

Build strong fundamentals in cybersecurity, networking, and cryptography — and set up a professional ethical hacking lab environment.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task1-notes.md` | Detailed notes covering all 6 topics of Task 1 |
| `task1-cheatsheet.md` | Quick reference for Linux, Nmap, Wireshark, OpenSSL, Netcat |
| `README.md` | This file |

---

## 🧪 Lab Setup

### Architecture
```
[Kali Linux — Attacker Machine]
            |
    Host-Only Network
    (192.168.56.x)
            |
[Metasploitable2 — Target Machine]
```

### Environment
| Component | Details |
|-----------|---------|
| **Attacker OS** | Kali Linux (Primary OS) |
| **Virtualization** | VirtualBox |
| **Target VM** | Metasploitable2 |
| **Network** | Host-Only Adapter |
| **Host Machine** | Ryzen 7 8700F, 32GB DDR5 |

---

## ✅ Topics Covered

### 1. Cybersecurity Basics
- CIA Triad — Confidentiality, Integrity, Availability
- Threat Types — Phishing, Malware, DDoS, SQLi, Brute Force, Ransomware
- Attack Vectors — Social Engineering, Wireless Attacks, Insider Threats

### 2. Lab Environment Setup
- Installed VirtualBox + Metasploitable2
- Configured Host-Only network adapter
- Verified connectivity between Kali and target VM

### 3. Linux Fundamentals
- File system navigation, permissions (chmod, chown)
- Package management (apt, dpkg)
- Networking commands (ip, netstat, ping, traceroute)

### 4. Networking Basics
- OSI Model — all 7 layers and functions
- TCP/IP protocol suite, TCP 3-way handshake
- DNS, HTTP/HTTPS, IP addressing and subnetting

### 5. Cryptography Basics
- Symmetric vs Asymmetric encryption
- Hashing — MD5, SHA256 using OpenSSL
- Digital certificates, SSL/TLS
- Hands-on: Encrypted and decrypted messages using OpenSSL AES-256

### 6. Tool Familiarization
- **Nmap** — Service version detection, OS detection, port scanning
- **Wireshark** — Packet capture, ICMP/HTTP traffic analysis
- **Burp Suite** — HTTP request interception via proxy
- **Netcat** — Listener setup, banner grabbing (SSH + HTTP)

---

## 🛠️ Tools Used

| Tool | Purpose | Command Used |
|------|---------|--------------|
| Nmap | Port & service scanning | `nmap -sV -O <target>` |
| Wireshark | Packet capture & analysis | ICMP filter, TCP stream |
| Burp Suite | Web proxy & request intercept | Manual proxy 127.0.0.1:8080 |
| Netcat | Banner grabbing & connectivity | `nc -lvp 4444`, `nc <ip> 22` |
| OpenSSL | Encryption & hashing | AES-256-CBC, SHA256 |

---

## 📦 Deliverables

- [x] Lab Setup Report (screenshots of Kali, Metasploitable2, Wireshark capture)
- [x] GitHub Repo with notes & Linux cheatsheet
- [x] 5-min Video walkthrough of lab setup

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](https://www.linkedin.com/posts/mr-manivel-r_cybersecurity-ethicalhacking-kalilinux-ugcPost-7478102713994489857-Jvxg/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGDJA9sBzSi23edH7UWChoU_mcEMAARlJJ8)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)
- 💼 **LinkedIn:** [linkedin.com/in/mr-manivel-r](https://www.linkedin.com/in/mr-manivel-r/)

---

> ⚠️ All activities performed in an isolated lab environment for educational purposes only.

*Manivel R | ApexPlanet Internship 2026 | Anna University*
