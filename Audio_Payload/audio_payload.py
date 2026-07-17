import os
import time
import subprocess
import threading
import ctypes

# ============================================================
# Audio Payload POC - PayloadParadise
# FOR EDUCATIONAL PURPOSES ONLY.
# ============================================================

# YouTube video to open (e.g., Rickroll or an annoying 10-hour loop)
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1"

def max_out_volume():
    """
    Maxes out the Windows system volume.
    Requires ctypes to interact with the Windows API to simulate the Volume Up keystroke.
    VK_VOLUME_UP is 0xAF.
    """
    VK_VOLUME_UP = 0xAF
    # We press it 50 times to ensure it hits 100% volume
    for _ in range(50):
        ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, 0, 0) # Key down
        ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, 2, 0) # Key up
        time.sleep(0.01)

def play_annoying_beeps():
    """
    Plays a series of high-pitched system beeps.
    Uses ctypes to access the kernel32 Beep function.
    """
    # Frequency in hertz, Duration in milliseconds
    patterns = [
        (2500, 200), (3000, 200), (2500, 200), (3000, 200),
        (3500, 100), (3500, 100), (3500, 100), (3500, 100)
    ]
    
    for freq, duration in patterns:
        ctypes.windll.kernel32.Beep(freq, duration)
        time.sleep(0.05)

def text_to_speech():
    """
    Uses a small PowerShell script to access the SAPI.SpVoice COM object
    and speak an annoying message.
    """
    message = "Warning. System compromised. You should not run untrusted scripts."
    ps_script = f"""
    Add-Type -AssemblyName System.Speech;
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer;
    $synth.Speak('{message}');
    """
    
    try:
        # We use subprocess to run the PowerShell command silently
        subprocess.run(
            ["powershell", "-Command", ps_script], 
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    except Exception as e:
        pass

def open_youtube_video():
    """
    Opens the default web browser to a specific YouTube URL.
    """
    try:
        # Use os.startfile to launch the URL in the default browser on Windows
        os.startfile(YOUTUBE_URL)
    except AttributeError:
        # Fallback if os.startfile is somehow not available (e.g., not strictly Windows)
        subprocess.run(["cmd", "/c", "start", YOUTUBE_URL], creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception:
        pass

if __name__ == "__main__":
    # 1. Max out the system volume first
    max_out_volume()
    
    # 2. Play the system beeps
    play_annoying_beeps()
    
    # 3. Speak the TTS message
    # Run in a separate thread so it doesn't block the video opening
    tts_thread = threading.Thread(target=text_to_speech)
    tts_thread.start()
    
    # 4. Open the YouTube video
    open_youtube_video()
    
    # Wait for the TTS to finish before exiting
    tts_thread.join()
