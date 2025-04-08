# Basic concept: This program will take an address from the user and will show the location on the map.
"""import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_geocoder-app")
address = input("Enter an address to map: ")

location = geolocator.geocode(address)
if location:
    lat, lon = location.latitude, location.longitude

else:
    print("Address not found. Defaulting to Blue City.")
    lat, lon = 52.2128, 20.9554

m = folium.Map(location=[lat, lon], zoom_start=15)
folium.Marker(
    location=[lat, lon],
    popup=f"{address}",
    icon=folium.Icon(color="purple")).add_to(m)
m.save("map.html")
import webbrowser
webbrowser.open("map.html")
"""

# Enhanced map display with geocoding error handling and improved default location.   
"""import folium
from geopy.geocoders import Nominatim
import webbrowser

# Initialize geolocator
geolocator = Nominatim(user_agent="my_geocoder-app")

# Get user input
address = input("Enter an address to map: ")

# Try to get geolocation data
try:
    location = geolocator.geocode(address, timeout=10)  # Added timeout
    if location:
        lat, lon = location.latitude, location.longitude
    else:
        raise ValueError("Address not found")
except Exception as e:
    print(f"Error: {e}. Defaulting to a known location.")
    lat, lon = 52.2128, 20.9554  # Default location

# Create a map
m = folium.Map(location=[lat, lon], zoom_start=15)

# Add a marker
folium.Marker(
    location=[lat, lon],
    popup=f"{address}",
    icon=folium.Icon(color="purple")
).add_to(m)

# Save & open map
m.save("map.html")
webbrowser.open("map.html")
"""


# Implemented reverse geocoding for full addresses, 
# support for multiple addresses, nearby places display, 
# user-adjustable zoom, and location data saving to a file.
"""
import folium
from geopy.geocoders import Nominatim
import webbrowser
import csv

# Initialize geolocator
geolocator = Nominatim(user_agent="my_geocoder-app")

# Get user input (multiple addresses supported)
addresses = input("Enter addresses separated by commas: ").split(",")

# Ask user for zoom level
try:
    zoom_level = int(input("Enter zoom level (default is 15): ") or 15)
except ValueError:
    zoom_level = 15

# Create map (default location)
m = folium.Map(location=[52.2128, 20.9554], zoom_start=zoom_level)

# Open CSV file to save locations
with open("locations.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Address", "Latitude", "Longitude"])

    # Process each address
    for address in addresses:
        address = address.strip()
        location = geolocator.geocode(address, timeout=10)

        if location:
            lat, lon = location.latitude, location.longitude

            # Reverse geocode to get full address
            reverse_location = geolocator.reverse((lat, lon), language="en")
            full_address = reverse_location.address if reverse_location else address

            # Add marker with full address
            folium.Marker(
                location=[lat, lon],
                popup=f"Exact Location: {full_address}",
                icon=folium.Icon(color="blue")
            ).add_to(m)

            # Add circle marker for nearby area
            folium.CircleMarker(
                location=[lat, lon],
                radius=100,
                color="red",
                fill=True,
                fill_color="red",
                fill_opacity=0.3
            ).add_to(m)

            # Save to CSV
            writer.writerow([full_address, lat, lon])

        else:
            print(f"Address '{address}' not found.")

# Save and open the map
m.save("map.html")
webbrowser.open("map.html")"""



# Enhanced user input validation, caching for performance, 
# customizable map types, distance calculator, dark mode, and screenshot saving.  
"""
import folium   # For creating interactive maps
from geopy.geocoders import Nominatim   # For converting addresses to coordinates
from geopy.distance import geodesic # For calculating distances between coordinates
import webbrowser   # For opening the generated map in a web browser
import csv  # For writing geolocation data to a CSV file 

# Initialize geolocator
geolocator = Nominatim(user_agent="my_geocoder-app")
location_cache = {}  # Store previous lookups to optimize API calls

# Get user input (Multiple addresses supported)
while True:
    addresses = input("Enter addresses separated by commas (or type 'exit' to quit): ").strip()
    if addresses.lower() == "exit":
        print("Exiting program.")
        exit()
    if addresses:
        addresses = addresses.split(",")
        break
    else:
        print("Invalid input. Please enter at least one address.")

# Ask user for zoom level
try:
    zoom_level = int(input("Enter zoom level (default is 15): ") or 15)
except ValueError:
    zoom_level = 15

# Allow user to choose map style
map_type = input("Choose map type - (1) OpenStreetMap, (2) Stamen Terrain, (3) CartoDB Positron: ")
map_types = {"1": "OpenStreetMap", "2": "Stamen Terrain", "3": "CartoDB Positron"}
selected_map = map_types.get(map_type, "OpenStreetMap")

# Ask if user wants Dark Mode
use_dark_mode = input("Enable Dark Mode? (yes/no): ").strip().lower()
if use_dark_mode == "yes":
    selected_map = "CartoDB dark_matter"

# Create map with default location
m = folium.Map(location=[52.2128, 20.9554], zoom_start=zoom_level, tiles=selected_map)

# Open CSV file to save locations
with open("locations.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Address", "Latitude", "Longitude"])

    # Process each address
    for address in addresses:
        address = address.strip()

        # Check cache before making an API call
        if address in location_cache:
            lat, lon = location_cache[address]
        else:
            location = geolocator.geocode(address, timeout=10)
            if location:
                lat, lon = location.latitude, location.longitude
                location_cache[address] = (lat, lon)  # Store in cache
            else:
                print(f"Address '{address}' not found. Skipping...")
                continue

        # Reverse geocode to get full address
        reverse_location = geolocator.reverse((lat, lon), language="en")
        full_address = reverse_location.address if reverse_location else address

        # Add marker with full address
        folium.Marker(
            location=[lat, lon],
            popup=f"Exact Location: {full_address}",
            icon=folium.Icon(color="blue")
        ).add_to(m)

        # Add a circle marker to highlight the area
        folium.CircleMarker(
            location=[lat, lon],
            radius=100,  # 100 meters
            color="red",
            fill=True,
            fill_color="red",
            fill_opacity=0.3
        ).add_to(m)

        # Save to CSV file
        writer.writerow([full_address, lat, lon])

# Ask user if they want to calculate distance between two locations
calculate_distance = input("Do you want to calculate the distance between two locations? (yes/no): ").strip().lower()
if calculate_distance == "yes":
    address1 = input("Enter first location: ")
    address2 = input("Enter second location: ")

    loc1 = geolocator.geocode(address1, timeout=10)
    loc2 = geolocator.geocode(address2, timeout=10)

    if loc1 and loc2:
        coords1 = (loc1.latitude, loc1.longitude)
        coords2 = (loc2.latitude, loc2.longitude)
        distance_km = geodesic(coords1, coords2).kilometers
        print(f"Distance between {address1} and {address2}: {distance_km:.2f} km")
    else:
        print("One or both locations not found. Unable to calculate distance.")

# Save & open map
m.save("map.html")
webbrowser.open("map.html")

# Screenshot Saving (Requires Selenium and Chrome WebDriver)
try:
    from selenium import webdriver

    # Capture screenshot of map
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("file:///path/to/map.html")  # Change path as needed
    driver.save_screenshot("map_screenshot.png")
    driver.quit()

    print("Screenshot saved as 'map_screenshot.png'.")

except Exception as e:
    print(f"Screenshot capture failed: {e}. Make sure you have Selenium installed and ChromeDriver available.")
"""
# End of the program.

# Script Overview:  
# 1. Geocodes a list of addresses to find latitude and longitude.  
# 2. Maps locations as markers on a visual map.  
# 3. Stores coordinates and addresses in a CSV file.  
# 4. Calculates distances between locations.  
# 5. Optionally captures a screenshot of the map.  