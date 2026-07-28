# Annoying Audio Payload

This script demonstrates a "creative payload" that causes system disruption and embarrassment by taking control of the computer's audio and browser. It is designed to be highly noticeable rather than stealthy, simulating the "unexpected scripts" category mentioned in the main repository objectives.

## How It Works

This payload uses only Python's standard library modules and Windows built-in commands, ensuring it executes smoothly even within restricted sandbox environments like the WhatsApp `.pyzw` context.

1. **Max Volume**: It uses `ctypes.windll.user32.keybd_event` to simulate pressing the Windows `Volume Up` key (`VK_VOLUME_UP`, 0xAF) 50 times in rapid succession, guaranteeing the system volume is at 100%.
2. **System Beeps**: It uses `ctypes.windll.kernel32.Beep` to play a sequence of high-pitched, abrasive system beeps.
3. **Text-to-Speech**: It spawns a hidden `powershell` subprocess to invoke the Windows `SAPI.SpVoice` COM object, reading an intimidating message aloud ("Warning. System compromised...").
4. **YouTube Launch**: Finally, it uses `os.startfile()` to launch the system's default web browser to a YouTube video (specifically, a Rickroll) set to autoplay.

## Why This Matters

While often used for pranks (like Rickrolling), this technique highlights how an unflagged script execution vulnerability can be weaponized for severe workplace disruption, embarrassment, or as a distraction while a more malicious payload runs in the background. It proves that an attacker can easily manipulate hardware states (like volume levels) and launch external applications (like a browser) without needing complex third-party libraries.

## Disclaimer

This repository is for **educational purposes only**. Do not use these scripts maliciously. The purpose is to raise awareness and inspire robust security practices.
