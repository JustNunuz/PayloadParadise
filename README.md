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

### Interesting Observations

My goal was to explore the worst-case scenario by simulating malware activity. To achieve this, I decided to create a keylogger and a data exfiltration tool using a reverse shell and keylogging functionality. Here’s a breakdown of my attempts and findings:


#### Attempt 1: Keylogger
**Short Description and Objective**:
- The keylogger was designed to capture keystrokes, including both regular keys (e.g., letters, numbers) and special keys (e.g., space, enter, shift).
- The objective was to log sensitive information, such as login credentials, and store it in a file (`Leak Creds\secrets\keylog.txt`).

**Results**:
- The keylogger successfully established a reverse TCP connection and sent heartbeat messages to the attacker, confirming that the basic communication framework was functional.
- However, it consistently failed to transmit the actual keystrokes (e.g., login credentials) when executed via WhatsApp for Windows, despite working perfectly in a controlled environment (e.g., running directly in VS Code).
- Debugging revealed no clear reason for the failure, suggesting that the execution environment imposed restrictions on accessing system APIs or network resources.


#### Attempt 2: Data Exfiltration Using Reverse Shell and Keylogger
**Short Description and Objective**:
- This attempt combined the keylogger with a data exfiltration mechanism to send logged keystrokes to Pastebin using their API.
- The script read API keys and other sensitive information from the `secrets` folder to ensure modularity and security.

**Results**:
- Similar to the keylogger, the data exfiltration script worked flawlessly in a controlled environment but failed to send data to Pastebin when executed via WhatsApp for Windows.
- The reverse shell and heartbeat messages worked as intended, but the script could not transmit the logged keystrokes, likely due to network restrictions or blocked API access in the execution environment.


#### Broader Implications
- These experiments demonstrate the challenges of executing advanced malicious actions in restricted environments, even when basic functionality (e.g., reverse shells, file manipulation) works as expected.
- The inconsistencies observed suggest that WhatsApp’s execution environment imposes significant restrictions, which could be leveraged to mitigate potential attacks.
- This exploration highlights the importance of understanding execution context, permissions, and environmental limitations when developing or testing exploits.


### Credits

This project would not have been possible without the foundational work of the security researcher who discovered the [vulnerability](https://www.linkedin.com/in/saumyajeetdas/). You can find their research and insights in the original [GitHub repository](https://github.com/SaumyajeetDas/WhatsApp-Exploit). Their efforts were pivotal in shedding light on this serious security issue, and I want to acknowledge their contribution to the field.

## Disclaimer

This repository is for **educational purposes only**. Do not use these scripts maliciously. The purpose is to raise awareness and inspire robust security practices.

## Stay Secure

This project emphasizes that security starts with awareness. Even as power users, we must remember that trust can be exploited.
