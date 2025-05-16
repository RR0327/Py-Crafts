import webbrowser

def find_city_on_google_earth(city_name):
    # Format the URl with the  search query
    google_earth_url = f'https://earth.google.com/web/search/{city_name}'

    # Open Google Earth in the default browser with the search query
    webbrowser.open(google_earth_url)

# Example: Find New York City on Google Earth
find_city_on_google_earth('New York City')