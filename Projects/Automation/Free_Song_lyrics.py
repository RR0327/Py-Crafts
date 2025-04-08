"""import lyricsgenius

Video = "https://youtu.be/Qhl0bocazGQ?si=pN0jAOVem8-sX8e0"

genius = lyricsgenius.Genius(Video)
name = input("Enter Artist Name: ")
artist = genius.search_artist(name)
song = input("Type your song for Lyrics: ")
song = artist.song(song)
print(song.lyrics)"""


import lyricsgenius

# Replace 'your_genius_api_key' with your actual Genius API Key
api_key = "your_genius_api_key"
genius = lyricsgenius.Genius(api_key)

# Prompt for artist name and song title
artist_name = input("Enter Artist Name: ")
song_title = input("Type your song for Lyrics: ")

# Search for the song
song = genius.search_song(song_title, artist_name)

# Display the lyrics
if song:
    print(f"Lyrics for '{song_title}' by {artist_name}:\n")
    print(song.lyrics)
else:
    print(f"Lyrics for '{song_title}' by {artist_name} were not found.")
