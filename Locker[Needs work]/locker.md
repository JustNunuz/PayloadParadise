# Screen Locker Script Overview

This script creates a **full-screen locker** that prevents access to the system until the correct password is entered. It uses `pyautogui` for mouse control and `tkinter` for the GUI. **For educational purposes only. Unauthorized use is prohibited.**

## How It Works

### Full-Screen Locker
- **GUI Setup**:
  - Creates a full-screen window using `tkinter`.
  - Displays a label prompting the user to enter a password.
  - Includes an entry field for password input.
- **Mouse Control**:
  - Disables `pyautogui`'s failsafe feature to prevent interruption.
  - Continuously moves the mouse to the center of the screen and clicks to keep the locker active.
- **Password Check**:
  - Listens for the `Ctrl+C` key combination.
  - If the entered password is `"root"`, the locker exits.

### Key Features
- **Full-Screen Mode**: Prevents access to other applications.
- **Mouse Lock**: Keeps the mouse focused on the locker window.
- **Password Protection**: Unlocks only when the correct password is entered.

## Code Breakdown

### GUI Setup
- **Full-Screen Window**: Created using `tkinter` with `-fullscreen` attribute.
- **Labels and Entry Field**: Displays instructions and a password input field.

### Mouse Control
- **Click and Move**: Continuously clicks and moves the mouse to the center of the screen to maintain focus.

### Password Check
- **Callback Function**: Checks if the entered password is `"root"` when `Ctrl+C` is pressed.
- **Loop**: Keeps the locker active until the correct password is entered.

## Status: Needs Work!

This means these scripts do not work a POCs of an exploit and I need to do more research into why