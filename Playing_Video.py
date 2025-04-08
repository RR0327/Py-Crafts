import pywhatkit

try:
    song = input("Enter Song Name: ")

    pywhatkit.playonyt(song)

    print("Sccessfully Played!")

except:
    print("An Unexcepted Error!")

    pywhatkit.playonyt


"""
# Code Explanation
- The code prompts the user for a song name and plays it on YouTube using the pywhatkit library, while handling any errors gracefully.
- If successful, it prints a confirmation message; otherwise, it shows an error message.

# playonyt Function Explanation
- The playonyt function searches and plays a YouTube video based on a given topic (like a song), with options to use an API and automatically open the video.
- It takes three parameters: the topic (required), and two optional booleans that control API usage and video playback behavior.
"""