# CAPTCHA = Completely Automated Public Turing test to tell Computers and Humans Apart.
"""
CAPTCHAs are automated tests designed to distinguish between human users and bots.
They present challenges that are easy for humans to solve but difficult for computers,
    ensuring that only legitimate users can access certain online resources.

CAPTCHA stands for the Completely Automated Public Turing test to tell Computers and Humans Apart.
These tools help differentiate real users from automated ones by providing challenges
    that are difficult for computers but relatively easy for humans.
"""

# Raw work
"""
import random
from captcha.audio import AudioCaptcha

def genrate_random_captcha(length=6):
    characters = '1234567890'
    captcha_text = ''.join(random.choices(characters, k=length))
    return captcha_text

audio = AudioCaptcha()
captcha_text = genrate_random_captcha()
print(f"Generated CAPTCHA text: {captcha_text}")
audio_captcha = audio.generate(captcha_text)
audio.write(captcha_text, 'AudioCaptcha.wav')
print("Audio CAPTCHA saved as 'AudioCaptcha.wav'")
"""
# This code generates a random audio CAPTCHA consisting of digits and saves it as an audio file.

# Using gTTs for better clarity and compatibility
"""
import random
from gtts import gTTS

def generate_random_captcha(length=6):
    characters = '1234567890'
    return ''.join(random.choices(characters, k=length))

# Generate random numeric CAPTCHA
captcha_text = generate_random_captcha()
print(f"Generated CAPTCHA text: {captcha_text}")

# Convert to audio with spaced digits for clarity
spoken_text = ' '.join(captcha_text)

# Create and save audio file
tts = gTTS(text=spoken_text, lang='en')
tts.save("AudioCaptcha_gtts.mp3")
print("Audio CAPTCHA saved as 'AudioCaptcha_gtts.mp3'")
"""
# This code generates a random audio CAPTCHA consisting of digits and saves it as an audio file using gTTS.
# Note: Ensure you have the gTTS library installed. You can install it using pip:
# pip install gTTS
# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.

# Modified version with user interaction, folder creation, and time limit


# random: for generating random characters/numbers
import random
# gTTS: Google Text-to-Speech to convert text to audio
from gtts import gTTS
# os, time, datetime: for file handling, timing, and folder naming
import os
import time
from datetime import datetime

# Generate CAPTCHA based on mode:
#   - Digits only
#   - Digits + letters
#   - Math expression (returns answer + spoken question)
def generate_captcha(mode='digits', length=6):
    if mode == 'digits':
        characters = '1234567890'
        return ''.join(random.choices(characters, k=length)), 'digits'
    elif mode == 'alphanumeric':
        characters = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.choices(characters, k=length)), 'alphanumeric'
    elif mode == 'math':
        a, b = random.randint(1, 9), random.randint(1, 9)
        return f"{a + b}", f"{a} + {b}"
    else:
        raise ValueError("Invalid CAPTCHA mode")

# === Save audio with gTTS ===
def save_audio(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# === Create folder for today ===
def create_output_folder():
    folder = datetime.now().strftime("captchas/%Y-%m-%d")
    os.makedirs(folder, exist_ok=True)
    return folder

# === Timer check ===
# Returns True if 30 seconds have passed since the CAPTCHA was shown
def is_expired(start_time, max_seconds=30):
    return (time.time() - start_time) > max_seconds

# === Main CAPTCHA logic ===
# Prompts user to choose CAPTCHA type
def run_audio_captcha():
    print("Audio CAPTCHA Generator")
    print("Choose CAPTCHA type:")
    print("1: Digits only")
    print("2: Digits + Letters")
    print("3: Simple Math (e.g., 3 + 4)")

# Generates CAPTCHA text and audio
    mode_input = input("Your choice (1/2/3): ").strip()
    if mode_input == '1':
        captcha_text, spoken_text = generate_captcha('digits')
    elif mode_input == '2':
        captcha_text, spoken_text = generate_captcha('alphanumeric')
    elif mode_input == '3':
        captcha_text, spoken_text = generate_captcha('math')
    else:
        print("Invalid option.")
        return

    print(f"🔐 CAPTCHA Text (for debug): {captcha_text}")

# Saves audio to a dated folder
    folder = create_output_folder()
    file_path = os.path.join(folder, "AudioCaptcha_gtts.mp3")
    # Spoken format for clarity
    spoken = ' '.join(spoken_text) if mode_input in ['1', '2'] else spoken_text
    save_audio(spoken, file_path)
    print(f"🎧 CAPTCHA saved at: {file_path}")

# Starts a 30-second timer
    start_time = time.time()

    # 3 attempts max
    for attempt in range(3):
        if is_expired(start_time):
            print("⏱️ Time expired! Please try again.")
            return
        user_input = input(f"Attempt {attempt + 1}/3 - Enter CAPTCHA: ").strip().upper()
        if user_input == captcha_text:
            print("✅ Correct! You're human. ✅")
            return
        else:
            print("Incorrect.")

# Ends if the user succeeds, fails 3 times, or time expires
    print("🔒 Too many failed attempts. Access denied.")

# Run it
# Calls run_audio_captcha() if script is run directly
if __name__ == "__main__":
    run_audio_captcha()

# This script generates an audio CAPTCHA based on user-selected types (digits, alphanumeric, or simple math).
# It saves the audio file using gTTS and allows the user to solve the CAPTCHA with a time limit and limited attempts.

"""
In the above code :
Features Included
------------------

| Label | Feature                                               |
| ----- | ----------------------------------------------------- |
| B | Limit: 3 attempts                                     |
| C | Timeout: 30 seconds                                   |
| E | User picks: digits-only, alphanumeric, or math-based  |
| F | Saves audio in a dated folder: `captchas/YYYY-MM-DD/` |

"""
# Sample ouput:
"""
Audio CAPTCHA Generator
Choose CAPTCHA type:
1: Digits only
2: Digits + Letters
3: Simple Math (e.g., 3 + 4)
Your choice (1/2/3): 3
🔐 CAPTCHA Text (for debug): 9
🎧 CAPTCHA saved at: captchas/2025-05-23/AudioCaptcha_gtts.mp3
Attempt 1/3 - Enter CAPTCHA: 8
Incorrect.
Attempt 2/3 - Enter CAPTCHA: 9
✅ Correct! You're human. ✅
"""

# Imports required libraries:
# - 
# - gTTS: Google Text-to-Speech to convert text to audio
# - os, time, datetime: for file handling, timing, and folder naming

# Function: generate_captcha()
# - Generates a random CAPTCHA based on selected mode:
#   - Digits only
#   - Digits + letters
#   - Math expression (returns answer + spoken question)

# Function: save_audio()
# - Uses gTTS to convert text into audio and save as an MP3 file

# Function: create_output_folder()
# - Creates a folder based on today’s date (e.g., captchas/2025-05-23)

# Function: is_expired()
# - Returns True if 30 seconds have passed since the CAPTCHA was shown

# Function: run_audio_captcha()
# - Main flow of the program:
#   1. Prompts user to choose CAPTCHA type
#   2. Generates CAPTCHA text and audio
#   3. Saves audio to a dated folder
#   4. Starts a 30-second timer
#   5. Gives the user 3 chances to enter the correct CAPTCHA
#   6. Ends if the user succeeds, fails 3 times, or time expires

# Main runner:
# - Calls run_audio_captcha() if script is run directly
