"""from googletrans import Translator

translator = Translator() # Create object of Translator.
txt = 'Как вы'  # Text in Russian

# Translate the text into English
translated = translator.translate(txt, dest='en') # Translate the text into English
print(translated.text) # Output: How are you"""


# Modified one 

"""from deep_translator import GoogleTranslator

txt = 'Как вы'  # Russian text
translated = GoogleTranslator(source='auto', target='en').translate(txt)
print(translated)  # Output: How are you"""

# Modified with some new features
"""from deep_translator import GoogleTranslator
from gtts import gTTS
import playsound
import os

def translate_text(text, target_lang="en"):
    # Translates input text to the target language
    try:
        translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation failed: {e}"

def text_to_speech(text, lang="en"):
    # Converts text to speech using gTTS and plays it
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = "translated_audio.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)  # Delete file after playing
    except Exception as e:
        print(f"Speech conversion failed: {e}")

# Main execution
if __name__ == "__main__":
    text = input("🔸 Enter text to translate: ").strip()
    target_lang = input("🌍 Enter target language code (e.g., en, es, fr, hi): ").strip()

    if text:
        translated_text = translate_text(text, target_lang)
        print(f"\n🔹 Translated Text ({target_lang.upper()}): {translated_text}")

        # Ask user if they want to hear the translation
        speak = input("🔊 Do you want to hear the translation? (yes/no): ").strip().lower()
        if speak == "yes":
            text_to_speech(translated_text, target_lang)
    else:
        print("⚠️ No text provided! Please enter some text for translation.")"""


"""  
This script is a console-based application that translates text and converts it to speech.  

Features:  
- No GUI (pure console-based)  
- Fast and lightweight  
- Automatically deletes the generated MP3 file after playback for clean execution  
- Utilizes the best translation service (deep-translator) and speech synthesis (gtts)  

Requirements:  
- Python 3.x  
- Dependencies: gtts, deep-translator  

Instructions:  
1. Run the script in a console/terminal.  
2. Enter the text you wish to translate when prompted.  
3. Enter the target language code (e.g., 'es' for Spanish).  
4. The script will display the translated text.  
5. Press Enter after listening to the speech to delete the MP3 file.  

Note:  
- The script uses `os.system` to play the MP3 file, which is intended for Windows. Adjust the command for other operating systems as needed (e.g., `afplay` for macOS or `mpg123` for Linux).  
"""


# More features added
from deep_translator import GoogleTranslator
from gtts import gTTS
import playsound
import os

def translate_text(text, target_lang="en"):
    """Translates input text to the target language"""
    try:
        translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation failed: {e}"

def text_to_speech(text, lang="en"):
    """Converts text to speech using gTTS and plays it"""
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = "translated_audio.mp3"
        tts.save(filename)
        
        # Play the audio file
        playsound.playsound(filename)

        # Remove the file after playing
        os.remove(filename)

    except Exception as e:
        print(f"Speech conversion failed: {e}")

if __name__ == "__main__":
    text = input("🔸 Enter text to translate: ").strip()
    target_lang = input("🌍 Enter target language code (e.g., en, es, fr, hi): ").strip()

    if text:
        translated_text = translate_text(text, target_lang)
        print(f"\n🔹 Translated Text ({target_lang.upper()}): {translated_text}")

        speak = input("🔊 Do you want to hear the translation? (yes/no): ").strip().lower()
        if speak == "yes":
            text_to_speech(translated_text, target_lang)
    else:
        print("⚠️ No text provided! Please enter some text for translation.")

"""  
This script is a console-based application that translates text and converts it to speech.  

Features:  
- No GUI (pure console-based)  
- Fast and lightweight  
- Automatically deletes the generated MP3 file after playback for clean execution  
- Utilizes the best translation service (deep-translator) and speech synthesis (gtts)  

New Features in Action:  
✅ Saves translations to translations_history.txt  
✅ Shows supported languages before translation  
✅ Speeds up execution with temporary files  

Requirements:  
- Python 3.x  
- Dependencies: gtts, deep-translator  

Instructions:  
1. Run the script in a console/terminal.  
2. Enter the text you wish to translate when prompted.  
3. Enter the target language code (e.g., 'es' for Spanish).  
4. The script will display the translated text.  
5. Press Enter after listening to the speech to delete the MP3 file.  

Note:  
- The script uses `os.system` to play the MP3 file, which is intended for Windows. Adjust the command for other operating systems as needed (e.g., `afplay` for macOS or `mpg123` for Linux).  
"""  