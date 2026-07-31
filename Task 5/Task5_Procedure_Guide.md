# Task 5 — Capstone: DVWA Web Application Penetration Test
## Step-by-Step Procedure Guide (Days 49–60)

---

## Day 49–50: Planning

1. Re-confirm lab is up: Kali (attacker) + Metasploitable2/DVWA target on a **host-only** VirtualBox network. `ip a` on both, ping each other to confirm connectivity.
2. Write the **scope document** (goes in the final report's Methodology section):
   - Target: DVWA (all 3 security levels: low, medium, high)
   - In scope: SQLi, XSS, CSRF, LFI/RFI, auth/session handling, brute-force resistance
   - Out of scope: underlying OS/Metasploitable2 services (that's Task 4 territory)
   - Rules of engagement: isolated lab only, no external targets
3. Draw the network diagram (provided as `network_diagram.svg` — edit target/attacker IPs to match your actual VM addresses).
4. Create the GitHub repo now (empty), so every day's work can be committed incrementally instead of one giant dump at the end. Use the structure in `README.md`.

---

## Day 51–53: Reconnaissance & Vulnerability Mapping

1. `nmap -sV -sC -p- <DVWA_IP>` — confirm Apache/PHP/MySQL versions.
2. `nikto -h http://<DVWA_IP>/dvwa` — quick web-server misconfig scan.
3. Log into DVWA, set security level to **low**, and walk every module once manually just to re-familiarize yourself (you did this in Task 3, this is the refresher).
4. Screenshot DVWA's built-in "View Source" for each module at each security level — you'll cite these in Findings to explain *why* an attack works or fails.

---

## Day 54–56: Exploitation (repeat each at low → medium → high)

### SQL Injection
- Manual: `' OR '1'='1` in the user-ID field; extract DB via `UNION SELECT`.
- Automated: `sqlmap -u "http://<IP>/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=...;security=low" --dump`
- Compare what breaks at medium (input sanitization) and high (prepared statements) — this comparison *is* your mitigation evidence.

### XSS
- Reflected: `<script>alert(document.cookie)</script>` in the query param.
- Stored: same payload in the guestbook module — confirm it fires on page reload for *other* sessions too.
- At high level, test whether DVWA's CSP header blocks the payload; capture the browser console CSP violation as evidence.

### CSRF
- Craft a standalone HTML page with an auto-submitting form pointing at DVWA's password-change endpoint. Host it locally (`python3 -m http.server`), visit it while logged into DVWA, confirm password changes.
- At high level, note the CSRF token requirement and show the same attack failing.

### File Inclusion
- LFI: `?page=../../../../etc/passwd`
- RFI: host a malicious PHP file on your Kali box, include it via the vulnerable parameter, confirm code execution (`phpinfo()` or a reverse shell payload).

### Burp Suite
- Intercept the login POST request, send to Repeater, tamper with parameters.
- Send login to Intruder, run a small credential list (DVWA's known default creds count as your baseline), document lockout behavior (DVWA has none by default — note this as a finding).

**Throughout:** screenshot every successful exploit, save every tool output to `/evidence/` in your repo, named `taskX_low.png`, `taskX_medium.png`, etc.

---

## Day 57: Incident Response Simulation

1. While running the Day 54–56 attacks, keep Apache access/error logs and MySQL general query log running (`tail -f` in a separate terminal, redirect to a file).
2. Run `scripts/log_detection.py` (provided) against the captured log file — it flags SQLi/XSS/LFI signatures with line numbers and timestamps.
3. **Containment demo:** pick one attack (e.g. the SQLi), identify the source IP in the log, block it: `sudo iptables -A INPUT -s <attacker_IP> -j DROP`. Confirm the DVWA app is unreachable from that IP afterward.
4. **Eradication demo:** switch DVWA security level from low → high for that vulnerability class, re-run the attack, show it now fails. This stands in for "patching."
5. Write the post-incident report section: timeline (timestamped), indicators of compromise (payload strings, source IP), containment action taken, eradication action taken, lessons learned.

---

## Day 58: Report Assembly

1. Open `DVWA_Pentest_Report_Template.docx` (provided) and fill in each section — it already has the structure (Executive Summary, Methodology, Findings-per-vulnerability with severity ratings, Mitigations, Incident Response Summary, Appendix).
2. Insert your screenshots into the Findings and Appendix sections.
3. Assign severity per finding using a simple scale (Critical/High/Medium/Low) — base it on: ease of exploitation × impact. SQLi and RFI should land Critical/High; CSRF/XSS typically Medium; missing lockout Low/Medium.
4. Export the final report to PDF for submission (`File → Export as PDF` in Word/LibreOffice, or use the `pdf` skill if working from this environment).

---

## Day 59: GitHub Repo Finalization

1. Push all scripts, evidence screenshots, and the report PDF (not just the .docx) to the repo.
2. Write the top-level `README.md` (provided) with a clear project overview — this is often the first thing a reviewer opens.
3. Make sure the repo is **public** before submission.

---

## Day 60: Video & Submission

1. Record the 12-minute walkthrough:
   - 0:00–1:30 — project overview, scope, objectives
   - 1:30–7:00 — live demo of 2–3 exploits (pick your strongest: SQLi + XSS + CSRF work well on camera)
   - 7:00–9:30 — incident response demo (log detection → containment)
   - 9:30–11:00 — mitigation walkthrough (low vs high security level comparison)
   - 11:00–12:00 — summary, lessons learned
2. Upload to LinkedIn under Featured, copy the link.
3. Confirm GitHub repo is public, copy the link.
4. Submit via ApexPlanet portal: Offer Letter ID **APSPL2640160**, Task 5, paste both links.

---

## Timing note

Your NIT-Trichy hackathon (Team MindMesh) runs through Aug 1. Task 5 spans Days 49–60 of the internship — treat Day 49–50 planning as something you can do in short breaks during/after the hackathon, and push the exploitation-heavy days (54–57) to once you're back at your full lab setup.
