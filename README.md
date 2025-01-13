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


### Challenges

I initially attempted to write an exploit for a keylogger that would not only open a reverse shell but also send keystrokes back to the attacker. However, this proved to be far more difficult than expected. Despite multiple attempts, the keylogger would successfully establish a reverse shell and even send heartbeat messages back to the attacker. But when it came to transmitting the actual keystrokes—such as login credentials—it simply refused to do so. After numerous iterations and debugging attempts, I couldn't pinpoint the exact reason for the failure. The keylogger should have worked in theory, but its execution was inconsistent, making it a challenging task to achieve the desired functionality.

### Credits

This project would not have been possible without the foundational work of the security researcher who discovered the [vulnerability](https://www.bleepingcomputer.com/news/security/whatsapp-for-windows-lets-python-php-scripts-execute-with-no-warning/). You can find their research and insights in the original [GitHub repository]([https://github.com/SaumyajeetDas/WhatsApp-Exploit]). Their efforts were pivotal in shedding light on this serious security issue, and I want to acknowledge their contribution to the field.

## Disclaimer

This repository is for **educational purposes only**. Do not use these scripts maliciously. The purpose is to raise awareness and inspire robust security practices.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/JustNunuz/payload-paradise.git
   cd payload-paradise
   ```
2. Test the scripts in a **controlled environment** (e.g., virtual machines or isolated systems).

## Stay Secure

This project emphasizes that security starts with awareness. Even as power users, we must remember that trust can be exploited.
