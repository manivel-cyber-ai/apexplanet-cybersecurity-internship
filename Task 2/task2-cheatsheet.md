# Task 2 — Quick Reference Cheatsheet
> Network Security & Scanning | ApexPlanet Internship

---

## 🔍 Reconnaissance

```bash
# PASSIVE RECON
whois domain.com                    # Domain info
nslookup domain.com                 # DNS lookup
nslookup -type=MX domain.com        # Mail servers
dig domain.com                      # Detailed DNS
dig domain.com ANY                  # All DNS records
dig -x <IP>                         # Reverse DNS

# GOOGLE DORKING
site:target.com
filetype:pdf site:target.com
intitle:"index of" site:target.com
inurl:admin site:target.com

# ACTIVE RECON
nmap -sn 192.168.56.0/24            # Ping sweep
nc 192.168.56.101 22                # Banner grab SSH
nc 192.168.56.101 80                # Banner grab HTTP
nc 192.168.56.101 21                # Banner grab FTP
```

---

## 🗺️ Nmap Full Reference

```bash
# SCAN TYPES
nmap -sS <IP>      # SYN stealth (needs root)
nmap -sT <IP>      # TCP connect (no root)
nmap -sU <IP>      # UDP scan
nmap -sA <IP>      # ACK scan (firewall detection)
nmap -sN <IP>      # NULL scan
nmap -sF <IP>      # FIN scan

# PORT SELECTION
nmap <IP>                    # Top 1000 ports
nmap -p- <IP>                # All 65535 ports
nmap -p 22,80,443 <IP>       # Specific ports
nmap -p 1-1000 <IP>          # Port range
nmap -F <IP>                 # Top 100 ports (fast)
nmap --top-ports 500 <IP>    # Top 500 ports

# DETECTION
nmap -sV <IP>                # Service versions
nmap -O <IP>                 # OS detection
nmap -A <IP>                 # All: OS+version+scripts

# NSE SCRIPTS
nmap -sC <IP>                          # Default scripts
nmap --script vuln <IP>                # Vulnerability scan
nmap --script ftp-vsftpd-backdoor <IP> # vsftpd backdoor
nmap --script smb-vuln-ms17-010 <IP>   # EternalBlue
nmap --script http-title <IP>          # Web titles
nmap --script ftp-anon <IP>            # Anonymous FTP

# OUTPUT
nmap -oN report.txt <IP>     # Normal text
nmap -oX report.xml <IP>     # XML
nmap -oG report.gnmap <IP>   # Grepable
nmap -oA report <IP>         # All formats
nmap -v <IP>                 # Verbose
nmap -vv <IP>                # Very verbose

# COMBINING FLAGS (FULL SCAN)
nmap -A -sV -O -p- -oN full-scan.txt 192.168.56.101
```

---

## 🦈 Wireshark Filters

```
# PROTOCOLS
http | ftp | ftp-data | dns | icmp | ssh | tcp | udp | arp

# IP FILTERS
ip.addr == 192.168.56.101
ip.src == 192.168.56.101
ip.dst == 192.168.56.101

# PORT FILTERS
tcp.port == 80
tcp.port == 21
udp.port == 53

# TCP FLAGS
tcp.flags.syn == 1                          # SYN packets
tcp.flags.syn == 1 && tcp.flags.ack == 0    # SYN flood
tcp.flags.rst == 1                          # RST packets
tcp.flags.fin == 1                          # FIN packets

# FTP CREDENTIALS
ftp contains "USER"
ftp contains "PASS"

# HTTP
http.request.method == "POST"
http.request.method == "GET"
http contains "password"
http.response.code == 200
http.response.code == 404

# COMBINE FILTERS
ip.addr == 192.168.56.101 && ftp
tcp.flags.syn == 1 && !tcp.flags.ack == 1
http || dns

# USEFUL ACTIONS
Right-click → Follow → TCP Stream
File → Export Objects → HTTP
Statistics → Protocol Hierarchy
Statistics → Conversations
Statistics → IO Graph
```

---

## 🔥 hping3 (SYN Flood Simulation)

```bash
# SYN flood (demo only — use in lab!)
hping3 -S --flood -V -p 80 192.168.56.101

# Flags explained:
# -S        → Send SYN packets
# --flood   → Send as fast as possible
# -V        → Verbose
# -p 80     → Target port 80

# Stop with Ctrl+C
# Then check Wireshark: tcp.flags.syn == 1
```

---

## 🛡️ iptables Cheatsheet

```bash
# VIEW RULES
iptables -L                  # List all rules
iptables -L -v -n            # Verbose + numeric
iptables -L INPUT            # INPUT chain only

# ADD RULES
iptables -A INPUT -p tcp --dport 22 -j DROP      # Block SSH
iptables -A INPUT -p tcp --dport 80 -j ACCEPT    # Allow HTTP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT   # Allow HTTPS
iptables -A INPUT -s 192.168.56.101 -j DROP      # Block IP
iptables -A INPUT -i lo -j ACCEPT                # Allow loopback

# DELETE RULES
iptables -D INPUT -p tcp --dport 22 -j DROP      # Delete specific
iptables -F                                       # Flush ALL rules
iptables -F INPUT                                 # Flush INPUT only

# DEFAULT POLICIES
iptables -P INPUT DROP        # Block all incoming by default
iptables -P INPUT ACCEPT      # Allow all incoming by default

# STATEFUL RULES
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# SAVE & RESTORE
iptables-save > /etc/iptables/rules.v4
iptables-restore < /etc/iptables/rules.v4
```

---

## 🌐 DNS Record Types

| Record | Purpose | Example |
|--------|---------|---------|
| A | IPv4 address | google.com → 142.250.x.x |
| AAAA | IPv6 address | google.com → 2607::... |
| MX | Mail server | gmail.com mail servers |
| NS | Name servers | authoritative DNS servers |
| CNAME | Alias/redirect | www → main domain |
| TXT | Text records | SPF, DKIM, verification |
| PTR | Reverse DNS | IP → domain name |

---

## 📊 CVSS Severity Scale

| Score | Severity | Action |
|-------|----------|--------|
| 9.0–10.0 | 🔴 Critical | Patch immediately |
| 7.0–8.9 | 🟠 High | Patch ASAP |
| 4.0–6.9 | 🟡 Medium | Plan to patch |
| 0.1–3.9 | 🟢 Low | Monitor |
| 0 | ℹ️ Info | Informational |

---

## 🔑 Key Port Reference

```
21   FTP          (plaintext — dangerous)
22   SSH          (encrypted — secure)
23   Telnet       (plaintext — dangerous)
25   SMTP         (email sending)
53   DNS          (TCP+UDP)
80   HTTP         (plaintext web)
110  POP3         (email retrieval)
139  NetBIOS      (Windows file sharing)
143  IMAP         (email)
443  HTTPS        (encrypted web)
445  SMB          (Windows shares — EternalBlue)
3306 MySQL        (database)
3389 RDP          (Windows remote desktop)
5432 PostgreSQL   (database)
8080 HTTP-Alt     (Tomcat, proxy)
8443 HTTPS-Alt    (Tomcat SSL)
```

---

*Cheatsheet by Manivel R | ApexPlanet Internship 2026 | github.com/manivel-cyber-ai*
