# Task 2: Network Security & Scanning
> ApexPlanet Cybersecurity Internship | Days 13–24

---

## 1. Reconnaissance

### What is Reconnaissance?
Reconnaissance (Recon) is the first phase of ethical hacking — gathering information about a target before attacking. It is divided into two types:

| Type | Description | Contact with Target |
|------|-------------|-------------------|
| **Passive Recon** | Gathering info without directly interacting with target | No |
| **Active Recon** | Directly interacting with target to gather info | Yes |

---

### Passive Reconnaissance Tools

#### Whois
```bash
whois google.com
whois 192.168.56.101
# Returns: registrar, creation date, name servers, contact info
```

#### Nslookup
```bash
nslookup google.com           # Basic DNS lookup
nslookup -type=MX google.com  # Mail server records
nslookup -type=NS google.com  # Name server records
nslookup -type=A google.com   # IPv4 address records
```

#### Dig (DNS Interrogation)
```bash
dig google.com                # Basic A record
dig google.com MX             # Mail records
dig google.com NS             # Name servers
dig google.com ANY            # All records
dig @8.8.8.8 google.com       # Query specific DNS server
dig -x 8.8.8.8                # Reverse DNS lookup
```

#### Google Dorking
```
site:target.com               # All pages from a domain
filetype:pdf site:target.com  # Find PDF files
intitle:"index of" site:target.com  # Directory listings
inurl:admin site:target.com   # Admin pages
"password" filetype:txt       # Exposed password files
```

#### Shodan
- Search engine for internet-connected devices
- Find open ports, services, banners without touching target
- Example searches: `apache 2.2.8`, `port:22 country:IN`

---

### Active Reconnaissance

#### Ping Sweep (Host Discovery)
```bash
nmap -sn 192.168.56.0/24      # Discover live hosts
nmap -sn 192.168.56.0/24 --open  # Show only up hosts
```

#### Banner Grabbing with Netcat
```bash
nc 192.168.56.101 22    # SSH banner
nc 192.168.56.101 80    # HTTP banner
nc 192.168.56.101 21    # FTP banner

# Manual HTTP request
nc 192.168.56.101 80
GET / HTTP/1.0
[press Enter twice]
```

---

## 2. Port & Service Scanning

### Nmap Scan Types

#### TCP SYN Scan (Stealth Scan)
```bash
nmap -sS 192.168.56.101
# Sends SYN, receives SYN-ACK (open) or RST (closed)
# Never completes 3-way handshake → harder to detect
# Requires root/sudo
```

#### TCP Connect Scan
```bash
nmap -sT 192.168.56.101
# Completes full 3-way handshake
# Slower, more detectable
# Works without root
```

#### UDP Scan
```bash
nmap -sU 192.168.56.101
# Scans UDP ports (DNS-53, DHCP-67, SNMP-161)
# Slower than TCP scans
sudo nmap -sU --top-ports 100 192.168.56.101
```

#### Service & Version Detection
```bash
nmap -sV 192.168.56.101
# Detects exact service versions running on open ports
```

#### OS Detection
```bash
nmap -O 192.168.56.101
# Detects operating system based on TCP/IP fingerprinting
```

#### Aggressive Scan (All-in-One)
```bash
nmap -A 192.168.56.101
# Includes: OS detection + version detection + script scanning + traceroute
```

#### Save Scan Report
```bash
nmap -A 192.168.56.101 -oN task2-nmap-report.txt   # Normal text
nmap -A 192.168.56.101 -oX task2-nmap-report.xml   # XML
nmap -A 192.168.56.101 -oA task2-nmap-report        # All formats
```

### Nmap Port States
| State | Meaning |
|-------|---------|
| **open** | Port is accepting connections |
| **closed** | Port is accessible but no service listening |
| **filtered** | Firewall is blocking the port |
| **unfiltered** | Port accessible but state unknown |
| **open\|filtered** | Cannot determine if open or filtered |

### Common Metasploitable2 Ports
| Port | Service | Version | Risk |
|------|---------|---------|------|
| 21 | FTP | vsftpd 2.3.4 | Critical (backdoor) |
| 22 | SSH | OpenSSH 4.7p1 | Medium |
| 23 | Telnet | Linux telnetd | High (plaintext) |
| 80 | HTTP | Apache 2.2.8 | High |
| 139/445 | SMB | Samba 3.0.20 | Critical |
| 3306 | MySQL | 5.0.51a | High |
| 5432 | PostgreSQL | 8.3.0 | Medium |
| 8180 | HTTP | Apache Tomcat | High |

---

## 3. Vulnerability Scanning

### OpenVAS (GVM) Setup
```bash
# Install
apt install openvas -y
gvm-setup          # Initial setup (takes ~10 min)
gvm-check-setup    # Verify installation
gvm-start          # Start the service

# Access UI
# Open browser → https://127.0.0.1:9392
# Default credentials set during gvm-setup
```

### Running a Scan
1. Login to OpenVAS web UI
2. Scans → Targets → New Target
3. Enter target IP: `192.168.56.101`
4. Scans → Tasks → New Task → select target
5. Click Start Scan (green play button)
6. Wait for completion → click report
7. Export as PDF

### Vulnerability Severity Levels (CVSS)
| Severity | CVSS Score | Action Required |
|----------|-----------|----------------|
| **Critical** | 9.0–10.0 | Immediate patch |
| **High** | 7.0–8.9 | Patch ASAP |
| **Medium** | 4.0–6.9 | Plan to patch |
| **Low** | 0.1–3.9 | Monitor |
| **Info** | 0 | Informational |

### Alternative: Nmap Vulnerability Scripts
```bash
# Vulnerability scan with NSE scripts
nmap --script vuln 192.168.56.101

# Specific vulnerability checks
nmap --script ftp-vsftpd-backdoor 192.168.56.101
nmap --script smb-vuln-ms17-010 192.168.56.101
nmap --script http-sql-injection 192.168.56.101
```

---

## 4. Packet Analysis with Wireshark

### Capturing Traffic
1. Open Wireshark
2. Select interface: `eth0` or `vboxnet0`
3. Click blue shark fin → Start capture
4. Generate traffic (ping, FTP, HTTP)
5. Click red square → Stop capture

### Key Filters for Task 2
```
# Protocol filters
http          → HTTP traffic only
ftp           → FTP control channel
ftp-data      → FTP data transfer
dns           → DNS queries/responses
icmp          → Ping traffic
tcp           → All TCP traffic

# SYN flood detection
tcp.flags.syn == 1 && tcp.flags.ack == 0

# FTP credentials
ftp contains "USER"
ftp contains "PASS"

# HTTP POST (login forms)
http.request.method == "POST"
```

### Capturing FTP Credentials (Plaintext Demo)
```bash
# Start Wireshark capture first, then:
ftp 192.168.56.101
# Enter: msfadmin / msfadmin

# In Wireshark filter: ftp
# You will see:
# USER msfadmin → in plaintext
# PASS msfadmin → in plaintext
```

### SYN Flood Simulation with hping3
```bash
# Simulate SYN flood (run briefly for demo only)
hping3 -S --flood -V -p 80 192.168.56.101

# In Wireshark:
# Filter: tcp.flags.syn == 1
# You'll see thousands of SYN packets from one source
```

### Following a TCP Stream
1. Right-click any packet in the stream
2. Follow → TCP Stream
3. See full conversation in readable format

---

## 5. Firewall Basics with iptables

### iptables Chain Structure
```
Incoming Traffic → INPUT chain
Forwarded Traffic → FORWARD chain
Outgoing Traffic → OUTPUT chain
```

### Basic Commands
```bash
# View current rules
iptables -L
iptables -L -v -n          # Verbose with packet counts

# Flush all rules (reset)
iptables -F

# Save and restore rules
iptables-save > /etc/iptables/rules.v4
iptables-restore < /etc/iptables/rules.v4
```

### Creating Rules
```bash
# Block incoming SSH (port 22)
iptables -A INPUT -p tcp --dport 22 -j DROP

# Allow HTTP (port 80)
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Block specific IP
iptables -A INPUT -s 192.168.56.101 -j DROP

# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Block all incoming by default
iptables -P INPUT DROP

# Allow loopback
iptables -A INPUT -i lo -j ACCEPT
```

### Demo: Block Port Scan
```bash
# Add rule to block Nmap SYN scans
iptables -A INPUT -p tcp --tcp-flags ALL SYN -j DROP

# Test from another terminal:
nmap -sS 192.168.56.101    # Should show all filtered

# Remove rule after demo:
iptables -F
```

---

## Key Concepts Summary

| Concept | Definition |
|---------|-----------|
| **Passive Recon** | Info gathering without touching target |
| **Active Recon** | Direct interaction with target |
| **Port Scanning** | Finding open ports on a target system |
| **Banner Grabbing** | Reading service banners to identify versions |
| **Vulnerability** | A weakness that can be exploited |
| **CVE** | Common Vulnerabilities and Exposures — public ID |
| **CVSS** | Score 0–10 measuring vulnerability severity |
| **Packet Sniffing** | Capturing network traffic for analysis |
| **SYN Flood** | DoS attack sending mass SYN packets |
| **Firewall** | Network security system filtering traffic |
| **iptables** | Linux kernel firewall rule management tool |
| **False Positive** | Vulnerability reported that doesn't actually exist |
| **False Negative** | Real vulnerability missed by scanner |

---

*Notes by Manivel R | ApexPlanet Cybersecurity Internship 2026*
