# Keylogger Script Overview

This script is a **keylogger** that captures keystrokes and logs them to a file. It runs for a specified duration before terminating. **For educational purposes only. Unauthorized use is prohibited.**

## How It Works

### Keylogging
- **Log File**:
  - Keystrokes are logged to a file located at `~/Desktop/keylog.txt`.
- **Key Press Handling**:
  - **Alphanumeric Keys**: Logs the character directly.
  - **Special Keys**: Maps special keys (e.g., space, enter, shift) to readable strings (e.g., `[space]`, `[enter]`).
- **Key Release Handling**:
  - Monitors key releases and stops the keylogger if the `esc` key is pressed.

### Time Limit
- The script runs for a **specified duration** (15 seconds by default).
- A separate thread monitors the elapsed time and terminates the program when the time limit is reached.

### Multithreading
- **Keylogger Thread**: Handles keylogging.
- **Timer Thread**: Monitors the time limit and exits the program when reached.

## Code Breakdown

### `on_press(key)`
- Logs keystrokes to the file.
- Handles both alphanumeric and special keys.

### `on_release(key)`
- Stops the keylogger if the `esc` key is released.

### `start_keylogger()`
- Starts the keylogger listener.

### `time_limit_check(duration)`
- Monitors the time limit and exits the program when reached.

### Main Execution
- Initializes and starts the keylogger and timer threads.
- Runs for the specified duration before terminating.

## Disclaimer
This script is for **educational and research purposes only**. Use only in environments where you have explicit permission.

## Status: Needs Work!

This means these scripts do not work a POCs of an exploit and I need to do more research into why