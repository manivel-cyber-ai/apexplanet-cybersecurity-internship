# Task 1 — Foundation & Environment Setup
> ApexPlanet Cybersecurity & Ethical Hacking Internship | Days 1–12

![Task](https://img.shields.io/badge/Task-1%20of%205-blue)
![Timeline](https://img.shields.io/badge/Timeline-Days%201--12-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Kali%20%7C%20Nmap%20%7C%20Wireshark%20%7C%20Burp%20Suite%20%7C%20Netcat-red)

---

## 🎯 Objective

Build strong fundamentals in cybersecurity, networking, and cryptography while setting up a professional ethical hacking lab environment.

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `task1-notes.md` | Detailed notes covering the main Task 1 topics |
| `task1-cheatsheet.md` | Quick reference for Linux, Nmap, Wireshark, OpenSSL, and Netcat |
| `Screenshots/` | Evidence screenshots from the lab setup and tool demonstrations |
| `README.md` | This file |

---

## 🧪 Lab Setup

### Architecture
```text
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
| **Attacker OS** | Kali Linux |
| **Virtualization** | VirtualBox |
| **Target VM** | Metasploitable2 |
| **Network** | Host-Only Adapter |
| **Host Machine** | Personal workstation |

---

## ✅ Topics Covered

### 1. Cybersecurity Basics
- CIA triad — confidentiality, integrity, and availability
- Threat types — phishing, malware, DDoS, SQL injection, brute force, and ransomware
- Attack vectors — social engineering, wireless attacks, and insider threats

### 2. Lab Environment Setup
- Installed VirtualBox and Metasploitable2
- Configured a host-only network adapter
- Verified connectivity between Kali and the target VM

### 3. Linux Fundamentals
- Filesystem navigation and permissions (`chmod`, `chown`)
- Package management (`apt`, `dpkg`)
- Networking commands (`ip`, `netstat`, `ping`, `traceroute`)

### 4. Networking Basics
- OSI model and its seven layers
- TCP/IP protocol suite and the TCP three-way handshake
- DNS, HTTP/HTTPS, IP addressing, and subnetting

### 5. Cryptography Basics
- Symmetric vs. asymmetric encryption
- Hashing with OpenSSL (for example, MD5 and SHA-256)
- Digital certificates and SSL/TLS
- Hands-on encryption and decryption using OpenSSL AES-256

### 6. Tool Familiarization
- **Nmap** — service detection, OS detection, and port scanning
- **Wireshark** — packet capture and traffic analysis
- **Burp Suite** — request interception through a proxy
- **Netcat** — listener setup and banner grabbing

---

## 🛠️ Tools Used

| Tool | Purpose | Example Command |
|------|---------|-----------------|
| Nmap | Port and service scanning | `nmap -sV -O <target>` |
| Wireshark | Packet capture and analysis | ICMP filter, TCP stream |
| Burp Suite | Web proxy and request interception | Manual proxy at `127.0.0.1:8080` |
| Netcat | Banner grabbing and connectivity | `nc -lvp 4444`, `nc <ip> 22` |
| OpenSSL | Encryption and hashing | AES-256-CBC, SHA-256 |

---

## 📦 Deliverables

- [x] Lab setup report with screenshots
- [x] GitHub repository with notes and a Linux cheatsheet
- [x] Short walkthrough video of the lab setup

---

## 🔗 Links

- 📹 **Video Walkthrough:** [LinkedIn Post](https://www.linkedin.com/posts/mr-manivel-r_cybersecurity-ethicalhacking-kalilinux-ugcPost-7478102713994489857-Jvxg/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGDJA9sBzSi23edH7UWChoU_mcEMAARlJJ8)
- 🌐 **Portfolio:** [manivel-cyber-ai.github.io](https://manivel-cyber-ai.github.io)
- 💼 **LinkedIn:** [linkedin.com/in/mr-manivel-r](https://www.linkedin.com/in/mr-manivel-r/)

---

> ⚠️ All activities were performed in an isolated lab environment for educational purposes only.

*Manivel R | ApexPlanet Internship 2026 | Anna University*
