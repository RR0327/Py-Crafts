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
# This code generates a random audio CAPTCHA consisting of digits and saves it as an audio file.