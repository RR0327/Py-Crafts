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
# This code generates a random audio CAPTCHA consisting of digits and saves it as an audio file using gTTS.
# Note: Ensure you have the gTTS library installed. You can install it using pip:
# pip install gTTS
# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.

