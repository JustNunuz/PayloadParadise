# Keylogger and Data Exfiltration PoC

This repository contains a **Proof of Concept (PoC)** for a keylogger and data exfiltration script. The keylogger captures keystrokes and exfiltrates the data to Pastebin using their API. 

## Scripts Overview

### `leak_cred.pyz`
- **Keylogging**:
  - Logs keystrokes to a file.
  - Handles both regular and special keys (e.g., space, enter, shift).
- **Data Exfiltration**:
  - Sends logged data to Pastebin via their API.
  - Reads API keys from the `secrets` folder.
- **Time Limit**:
  - Runs for **20 seconds** before exfiltrating data.

### `data_exif.py`
- **Keylogging**:
  - Logs keystrokes to `Leak Creds\secrets\keylog.txt`.
  - Handles regular and special keys.
- **Data Exfiltration**:
  - Sends logged data to Pastebin using their API.
  - Reads API keys from the `secrets` folder.
- **Time Limit**:
  - Runs for **15 seconds** before exfiltrating data.

## Status: Needs Work!

This means these scripts do not work a POCs of an exploit and I need to do more research into why