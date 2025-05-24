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

# Modified version
from geopy.geocoders import Nominatim

def lookup_location_by_code(postal_code: str, country: str) -> None:
    """
    Lookup the location using postal code and country name.
    """
    geolocator = Nominatim(user_agent="global_postal_lookup_app")
    query = f"{postal_code}, {country}"

    try:
        location = geolocator.geocode(query, timeout=10)
        if location:
            print(f"\n📍 Location Details for '{postal_code}' in '{country}':")
            print(f"Address: {location.address}")
            print(f"Latitude: {location.latitude}")
            print(f"Longitude: {location.longitude}")
        else:
            print(f"\n No location found for '{postal_code}' in '{country}'.")
    except Exception as e:
        print(f"\n Error: {e}")

def main():
    print("🌍 Global ZIP/PIN Code Lookup Tool")

    postal_input = input("Enter ZIP code or PIN code: ").strip()
    country_input = input("Enter country name (e.g. USA, India, Canada): ").strip()

    lookup_location_by_code(postal_input, country_input)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nLookup another? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Goodbye!")
            break
"""
✅ Summary
Feature	                            Included
Accepts ZIP or PIN codes	            ✅
Supports all countries	                ✅
Shows full address & coordinates	    ✅
Clean error handling	                ✅
User-friendly interface             	✅
"""