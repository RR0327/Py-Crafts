# User input url

"""import pyshorteners

long_url = input("Enter the url to shorten: ")

type_tiny = pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(long_url)

print("The shortened URL is: " + short_url)"""





# Already input url

"""import pyshorteners

long_url = "https://www.example.com"

try:
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    print("The shortened URL is:", short_url)
except Exception as e:
    print("An error occurred:", e)"""
