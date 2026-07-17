# 🏝️ PayloadParadise — New POC Ideas

## Current Coverage Analysis

Here's what you **already have** and what's **missing**:

| Category | Existing POCs | Coverage |
|---|---|---|
| Remote Access | Reverse Shell ✅ | Solid |
| Reconnaissance | System metadata, processes, network, disk, env vars ✅ | Solid |
| File Operations | File Reading/Exfil ✅, Deletion ✅, Corruption (Doc + PDF) ✅ | Solid |
| Credential Theft | Keylogger ⚠️ (broken), Leak Creds ⚠️ (broken) | Needs work |
| System Lockout | Screen Locker ⚠️ (broken) | Needs work |
| **Persistence** | ❌ Nothing | **Major gap** |
| **Social Engineering** | ❌ Nothing | **Major gap** |
| **Network Attacks** | ❌ Nothing | **Major gap** |
| **Evasion / Anti-Forensics** | ❌ Nothing | **Major gap** |
| **Clipboard / Input Hijacking** | ❌ Nothing | **Major gap** |
| **Privilege Escalation** | ❌ Nothing | **Major gap** |

---

## 🔴 Tier 1 — High Impact, High Feasibility

These use **Python stdlib or near-stdlib modules** and are most likely to work in the `.pyzw` execution context (based on what already works: sockets, `os`, `subprocess`, `json`, `psutil`).

---

### 1. 📋 Clipboard Hijacker (Crypto Address Swap)
**Category:** Credential Harvesting / Financial  
**Description:** Monitor the clipboard for cryptocurrency wallet addresses (BTC, ETH patterns via regex). When detected, silently replace with the attacker's address. Victim copies a friend's wallet, pastes the attacker's.  
**Why it fits:** Clipboard access via `ctypes` on Windows is stdlib — no `pip install` needed. This is a *real* attack vector used in production malware.  
**Modules:** `ctypes`, `re`, `time`  
**Feasibility:** ⭐⭐⭐⭐⭐ — Very likely to work in `.pyzw` context.

---

### 2. 🔑 Wi-Fi Password Harvester
**Category:** Credential Harvesting  
**Description:** Run `netsh wlan show profiles` and then `netsh wlan show profile name="X" key=clear` for each saved network. Extract SSIDs and plaintext passwords, then exfiltrate via TCP.  
**Why it fits:** Pure `subprocess` + `socket` — both already proven to work in your existing POCs.  
**Modules:** `subprocess`, `socket`, `re`  
**Feasibility:** ⭐⭐⭐⭐⭐ — Extremely likely to work. This is essentially a recon variant.

---

### 3. 🪝 Startup Persistence (Registry / Startup Folder)
**Category:** Persistence  
**Description:** Copy the payload to `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\` or write a `Run` registry key via `reg add`. Ensures the payload survives reboots.  
**Why it fits:** File copy + `subprocess` for `reg add`. No special libs needed.  
**Modules:** `shutil`, `os`, `subprocess`  
**Feasibility:** ⭐⭐⭐⭐⭐ — Proven primitives.

---

### 4. 📸 Screenshot Capture & Exfiltration
**Category:** Reconnaissance / Espionage  
**Description:** Take periodic screenshots using `ctypes` to call Windows GDI APIs, save as BMP, and exfiltrate over TCP. No `Pillow` needed.  
**Why it fits:** Demonstrates visual espionage without any `pip` dependencies. Can be combined with your existing TCP exfil pattern.  
**Modules:** `ctypes`, `socket`, `struct`  
**Feasibility:** ⭐⭐⭐⭐ — `ctypes` GDI calls are well-documented.

---

### 5. 🗓️ Scheduled Task Persistence
**Category:** Persistence  
**Description:** Use `subprocess` to call `schtasks /create` and register the payload as a scheduled task that runs at logon or on a timer. More stealthy than startup folder.  
**Why it fits:** Pure `subprocess`, same pattern as your recon POC.  
**Modules:** `subprocess`, `os`  
**Feasibility:** ⭐⭐⭐⭐⭐ — If reverse shell works, this works.

---

### 6. 🌐 Browser Credential Extraction (Chrome/Edge)
**Category:** Credential Harvesting  
**Description:** Read Chrome/Edge's `Login Data` SQLite database from `%LOCALAPPDATA%`. Decrypt passwords using `CryptUnprotectData` via `ctypes`. Exfiltrate over TCP.  
**Why it fits:** `sqlite3` is stdlib. `CryptUnprotectData` is accessible via `ctypes`. This is a *very* common real-world payload.  
**Modules:** `sqlite3`, `ctypes`, `os`, `shutil`, `socket`  
**Feasibility:** ⭐⭐⭐⭐ — Depends on whether DPAPI calls work in the `.pyzw` context.

---

### 7. 📂 Document Hunter & Exfiltrator
**Category:** Data Exfiltration  
**Description:** Walk the filesystem (`os.walk`) looking for files matching patterns (`.docx`, `.xlsx`, `.pdf`, `.txt`, `.csv`, `.kdbx`). Log paths and sizes, optionally exfiltrate small files over TCP.  
**Why it fits:** Pure `os` + `socket`. A more targeted version of your existing file reading POC.  
**Modules:** `os`, `socket`, `json`  
**Feasibility:** ⭐⭐⭐⭐⭐ — `os.walk` is guaranteed to work.

---

## 🟠 Tier 2 — Medium-High Impact, Good Feasibility

---

### 8. 🎭 Fake Windows Update / UAC Prompt (Phishing GUI)
**Category:** Social Engineering  
**Description:** Display a convincing fake Windows Update screen or UAC dialog using `tkinter` (stdlib). Capture the password the user enters and exfiltrate it.  
**Why it fits:** `tkinter` is Python stdlib and your locker POC already uses it (partially works). This takes it further with credential capture.  
**Modules:** `tkinter`, `socket`, `ctypes` (for window styling)  
**Feasibility:** ⭐⭐⭐⭐ — `tkinter` works, the question is how convincing you can make the GUI.

---

### 9. 🔒 File Encryptor (Ransomware Simulator)
**Category:** System Disruption  
**Description:** Walk `Desktop` / `Documents`, XOR-encrypt files with a key, rename with `.locked` extension. Display a `tkinter` ransom note. Include a decryption routine for safe demo.  
**Why it fits:** Pure stdlib. This is the evolution of your existing File Corruption POC but with reversible encryption.  
**Modules:** `os`, `tkinter`, `struct`  
**Feasibility:** ⭐⭐⭐⭐ — All stdlib. Include a hardcoded "demo" decryption key for safety.

> [!CAUTION]
> This POC must include a prominent disclaimer, a limited scope (e.g., only target a test folder), and an easy decryption mechanism. Document it as a simulation only.

---

### 10. 🔊 Audio Eavesdropping (Microphone Capture)
**Category:** Espionage  
**Description:** Use `ctypes` to call Windows Multimedia APIs (`winmm.dll`) to record audio from the microphone, save as WAV, and exfiltrate.  
**Why it fits:** No `pyaudio` needed — `winmm.dll` is accessible via `ctypes` on all Windows machines.  
**Modules:** `ctypes`, `wave`, `socket`  
**Feasibility:** ⭐⭐⭐ — More complex `ctypes` work, but documented approaches exist.

---

### 11. 📡 DNS Exfiltration
**Category:** Data Exfiltration / Evasion  
**Description:** Encode stolen data into DNS query subdomains (e.g., `base64chunk.attacker.com`). Exfiltrates data that bypasses most firewalls since DNS is almost never blocked.  
**Why it fits:** Uses `socket` for raw DNS queries. Demonstrates an evasion technique your other POCs don't cover.  
**Modules:** `socket`, `base64`, `struct`  
**Feasibility:** ⭐⭐⭐⭐ — DNS is rarely blocked, making this very practical.

---

### 12. 📧 Email Self-Propagation (SMTP Worm Concept)
**Category:** Propagation / Social Engineering  
**Description:** Use `smtplib` (stdlib) to send the payload as an attachment to contacts harvested from the system. Demonstrates worm-like self-spreading behavior.  
**Why it fits:** `smtplib` is stdlib. Combine with your recon data to harvest contacts.  
**Modules:** `smtplib`, `email`, `os`  
**Feasibility:** ⭐⭐⭐ — SMTP sending works, but you'd need credentials or an open relay.

---

### 13. 🖥️ Webcam Snapshot
**Category:** Espionage  
**Description:** Use `ctypes` to interface with DirectShow or `avicap32.dll` to capture a single webcam frame, save it, and exfiltrate.  
**Why it fits:** Demonstrates physical surveillance capability — a major escalation from your current POCs.  
**Modules:** `ctypes`, `socket`  
**Feasibility:** ⭐⭐⭐ — More complex ctypes, but `avicap32` approaches are well-documented.

---

## 🟡 Tier 3 — Creative / Niche / Research-Grade

---

### 14. 🕰️ Timestamp Manipulator (Anti-Forensics)
**Category:** Anti-Forensics  
**Description:** Modify file creation/modification timestamps on specific files using `os.utime()` and `ctypes` for creation time. Cover tracks by making malicious files look old.  
**Why it fits:** Pure stdlib. Demonstrates anti-forensics — a category you don't have at all.  
**Modules:** `os`, `ctypes`, `datetime`  
**Feasibility:** ⭐⭐⭐⭐⭐ — `os.utime()` is trivial.

---

### 15. 🧹 Log Cleaner
**Category:** Anti-Forensics  
**Description:** Clear Windows Event Logs using `subprocess` to call `wevtutil cl System`, `wevtutil cl Security`, etc. Remove traces of the payload execution.  
**Why it fits:** Pure `subprocess`. Pairs naturally with your reverse shell POC as a post-exploitation step.  
**Modules:** `subprocess`  
**Feasibility:** ⭐⭐⭐⭐ — May require admin privileges, but worth demonstrating.

---

### 16. 🌍 ARP Spoof / Network Scanner
**Category:** Network Attacks  
**Description:** Use raw sockets to perform ARP scanning of the local subnet, discovering other devices. Optionally demonstrate ARP spoofing concepts.  
**Why it fits:** Fills the "Network Attacks" gap entirely.  
**Modules:** `socket`, `struct`, `subprocess` (for `arp -a`)  
**Feasibility:** ⭐⭐⭐ — Raw sockets may need admin on Windows.

---

### 17. 🎵 Annoying Audio Payload (Creative)
**Category:** Creative / System Disruption  
**Description:** Use `winsound` (stdlib) or `ctypes` + `Beep()` to play obnoxious sounds, text-to-speech via `SAPI.SpVoice` COM object, or max out the volume. A "creative payload" like your README mentions.  
**Why it fits:** `winsound` is Windows stdlib. Demonstrates the "unexpected scripts" category from your README.  
**Modules:** `winsound`, `ctypes`, `subprocess`  
**Feasibility:** ⭐⭐⭐⭐⭐ — `winsound.Beep()` is trivial.

---

### 18. 🔄 Wallpaper Changer
**Category:** Creative / System Disruption  
**Description:** Download an image (or generate one with text) and set it as the desktop wallpaper via `ctypes` calling `SystemParametersInfoW`. Display a message, meme, or warning.  
**Why it fits:** Single `ctypes` call. Low-effort, high-visual-impact creative payload.  
**Modules:** `ctypes`, `urllib.request`  
**Feasibility:** ⭐⭐⭐⭐⭐ — One API call.

---

### 19. 🗃️ Shadow Copy Deletion
**Category:** System Disruption / Anti-Recovery  
**Description:** Run `vssadmin delete shadows /all /quiet` via `subprocess`. Prevents file recovery — a technique used by real ransomware.  
**Why it fits:** Single `subprocess` call. Pairs with the file encryptor POC.  
**Modules:** `subprocess`  
**Feasibility:** ⭐⭐⭐⭐ — Requires admin, but demonstrates the threat.

---

### 20. 💾 USB Dropper / Spreader
**Category:** Propagation  
**Description:** Monitor for USB drive insertion (poll `os.path.exists` on drive letters). When detected, copy the payload to the USB with an autorun-style lure.  
**Why it fits:** Pure `os` + `shutil`. Shows physical propagation vector.  
**Modules:** `os`, `shutil`, `time`  
**Feasibility:** ⭐⭐⭐⭐ — Autorun is disabled by default on modern Windows, but the file copy still works as a social engineering lure.

---

## 📋 Recommended Build Order

Based on impact, feasibility, and filling gaps in your current coverage:

| Priority | POC | Why First |
|---|---|---|
| 1 | **Wi-Fi Password Harvester** | Easiest win — reuses your exact existing patterns (`subprocess` + `socket`) |
| 2 | **Clipboard Hijacker** | High-impact, real-world relevance, pure stdlib |
| 3 | **Startup Persistence** | Fills the biggest gap — no persistence POC exists |
| 4 | **Screenshot Capture** | Visual espionage is compelling for demos |
| 5 | **Fake UAC Prompt** | Social engineering gap + builds on your `tkinter` work |
| 6 | **Document Hunter** | Natural evolution of File Reading POC |
| 7 | **Timestamp Manipulator** | Opens the anti-forensics category |
| 8 | **File Encryptor** | Evolution of File Corruption — very high impact for presentations |
| 9 | **DNS Exfiltration** | Demonstrates evasion techniques |
| 10 | **Wallpaper Changer / Audio** | Quick creative payloads for showmanship |

---

> [!IMPORTANT]
> **Execution context insight from your README:** Your keylogger and data exfil POCs failed when executed via WhatsApp but worked in VS Code. This suggests the `.pyzw` context may restrict certain system API hooks (keyboard listeners) or network calls to specific endpoints. **Prioritize POCs that use `subprocess` to call Windows built-in commands** (like the Wi-Fi harvester) — these are most likely to work because your recon and reverse shell already prove that `subprocess` works reliably in this context.

> [!TIP]
> For the broken POCs (Keylogger, Leak Creds, Locker), consider rewriting them to use `subprocess` + `powershell` commands instead of Python-native libraries like `pynput`. For example, PowerShell's `Register-ObjectEvent` or `Get-Clipboard` may bypass whatever restrictions the WhatsApp execution sandbox imposes.
