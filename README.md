```

░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░    
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░    
░▒▓███████▓▒░░▒▓████████▓▒░░▒▓██████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████▓▒░   
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░    
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░    
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░       ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░ 
                                                                                                                                                                                                
                                                                                                                                                                                                

```

# Payload Paradise

Welcome to **Payload Paradise**, a repository showcasing proof-of-concept scripts that demonstrate the dangers of unflagged script execution vulnerabilities. This project explores the implications of the WhatsApp for Windows [vulnerability](https://www.bleepingcomputer.com/news/security/whatsapp-for-windows-lets-python-php-scripts-execute-with-no-warning/) that allows Python and PHP scripts to execute without warning.

## Objectives

- To highlight potential attack vectors from trusted applications executing scripts.
- To showcase real-world examples of what could go wrong if such vulnerabilities fall into the wrong hands.
- To stress the importance of handling trusted files with care, as even those from familiar sources can be harmful.

## System Information

I ran this on Windows 11 with WhatsApp 2.2450.6.0 from Dec 2024 to Jan 2025, and the vulnerability was still working. For all tests requiring another machine (attacker), I used a basic install of Kali Linux, unless stated otherwise.

## Contents

- **Reverse Shells**: Demonstrating unauthorized remote access.
- **System Reconnaissance**: Gathering metadata and user information.
- **File Manipulation**: Reading, writing, and deleting files.
- **System Interruption**: Shutting down the system or disrupting processes.
- **Creative Payloads**: Unexpected scripts showcasing how trusted apps can execute malicious code.

### Execution  

The scripts in this repository are provided in two file formats: `.pyz` and `.pyzw`. Here's a brief explanation of the difference between `.py`, `.pyz`, and `.pyzw` formats:

| File Format | Description                                                      | Behavior in WhatsApp                                                                                                     |
| ----------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **`.py`**   | The standard Python script you may be familiar with.             | **Blocked** by WhatsApp. These files will not execute as intended due to built-in security mechanisms.                   |
| **`.pyz`**  | A compressed Python archive.                                     | **Runs**, but opens a command prompt (CMD) window first, making it easier for the user to detect the script's execution. |
| **`.pyzw`** | A further-obfuscated format combining compression and packaging. | **Runs** without any noticeable background activity, making it more stealthy and harder for users to detect.             |

The repository only contains `.pyz` and `.pyzw` formats, each demonstrating different levels of detection and execution, providing insights into how scripts can bypass security measures and user awareness.

### How the Vulnerability Works

*   **Unblocked Extensions:** While WhatsApp blocks dangerous file formats like `.exe`, `.bat`, and `.scr`, it fails to block or warn users about Python script extensions such as `.pyz` and `.pyzw` (or PHP scripts).
*   **Direct Execution:** If the recipient has Python installed on their Windows computer, clicking "Open" on the file inside the chat runs the embedded script immediately using the system's default file association.
*   **Requirements:** The target device must have Python installed for the payload to execute. A `.pyz` file runs in the command line, while a `.pyzw` file runs without showing a command prompt window.
*   **Meta's Response:** Meta declined to issue a direct patch, stating it relies on user caution rather than expanding the client-side blocklist.

### How to Protect Yourself

*   **Never open unsolicited files:** Avoid clicking "Open" on any file sent via WhatsApp from unknown or untrusted contacts.
*   **Change file associations:** Reassociate `.pyz` and `.pyzw` extensions in Windows so they open with a text editor (like Notepad) instead of executing automatically with the Python interpreter.

*(Would you like instructions on how to change file associations in Windows or how to check if Python is configured on your system?)*

### Behavioral Failures

**Windows Defender:**
*   **Signature Integrity Verification:** Windows Defender relies on file signatures to identify known malware. However, when the `.pyz` file is sent and opened via WhatsApp, Defender does not adequately verify the signature. This occurs because WhatsApp does not provide sufficient metadata for Defender to identify the file as a threat.
*   **Execution Blocking:** The real-time protection of Windows Defender is bypassed by WhatsApp when opening `.pyz` files, allowing execution without blocking.

**UAC (User Account Control):**
*   **Permission Request:** UAC does not request administrative permission when executing `.pyz` files from WhatsApp. This is due to a failure in the security context integration between WhatsApp and the operating system, where the file is treated as trusted content, allowing privilege escalation.

**WhatsApp:**
*   **Security Verification:** WhatsApp does not perform adequate security checks when opening `.pyz` files. This means there is no behavioral analysis of the file before execution, nor integrity or origin verification.
*   **User Notification:** WhatsApp does not implement a security notification or confirmation before executing potentially dangerous files. This leaves users vulnerable to automatic malware executions.

**Antivirus Software:**
*   **Malware Detection:** Many antivirus programs rely on real-time scanning and file signatures. However, the execution of `.pyz` files through WhatsApp is not properly intercepted, allowing malware to go undetected.
*   **Payload Blocking:** The execution of malicious payloads establishing remote connections (such as reverse shells) is not blocked when the `.pyz` file is executed via WhatsApp. This is due to a failure in deep packet inspection and network behavior analysis by antivirus programs, especially when the file is initiated by a trusted application like WhatsApp.

### Credits

This project would not have been possible without the foundational work of the security researcher who discovered the [vulnerability](https://www.linkedin.com/in/saumyajeetdas/). You can find their research and insights in the original [GitHub repository](https://github.com/SaumyajeetDas/WhatsApp-Exploit). Their efforts were pivotal in shedding light on this serious security issue, and I want to acknowledge their contribution to the field.


