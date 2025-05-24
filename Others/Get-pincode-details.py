# Raw
"""
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_zipcode_lookup_tool")

zip_data = input("Enter the ZIP code: ").strip()

try:
    location = geolocator.geocode(zip_data, timeout=10)
    if location:
        print("Zipcode:", zip_data)
        print("Details of the Zipcode:")
        print(location)
    else:
        print("No location found for this ZIP code.")
except Exception as e:
    print(f"Error occurred: {e}")
"""
"""
✅ What They Do:
  Package	    Purpose
• geopy	        Geocoding (convert address ↔ coordinates), distance, etc. using providers like Nominatim, Google, etc.
• geocoder	    A user-friendly wrapper for geocoding services (IP, address lookup, etc.)
"""
# Explanation of the code
"""
• The user_agent is required by the OpenStreetMap API to identify the client.
• "my_zipcode_lookup_tool" is a custom, unique name, which avoids 403 errors.
• strip() is a string method that removes leading and trailing whitespace.

✅ Why .strip() is important:
• It cleans up any accidental spaces the user typed before or after the ZIP code.
• Without it, geocode(" 90210 ") might fail or produce incorrect results.
"""

