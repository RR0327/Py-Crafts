import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import process

# Add more countries/cities as needed
KNOWN_CITIES = {
    "usa": ["new-york", "los-angeles", "chicago", "houston"],
    "uk": ["london", "manchester", "birmingham"],
    "bangladesh": ["dhaka", "chittagong", "khulna"],
    "japan": ["tokyo", "osaka", "kyoto"],
    "india": ["delhi", "mumbai", "bangalore"],
}

def suggest_city(country, city):
    country = country.lower().strip()
    city = city.lower().strip().replace(" ", "-")
    if country in KNOWN_CITIES:
        best_match = process.extractOne(city, KNOWN_CITIES[country])
        if best_match and best_match[1] >= 80:
            return best_match[0]
    return city

def get_weather_data(country, city):
    country = country.lower().strip().replace(" ", "-")
    city = suggest_city(country, city)
    url = f"https://www.timeanddate.com/weather/{country}/{city}"

    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        temperature = soup.find("div", class_="h2").get_text(strip=True)
        condition_div = soup.find("div", class_="bk-focus__qlook")
        condition = condition_div.find("p").get_text(strip=True)

        sunrise = sunset = "Not found"
        table = soup.find("table", class_="table table--left table--inner-borders-rows")
        if table:
            rows = table.find_all("tr")
            for row in rows:
                if "Sunrise" in row.text:
                    sunrise = row.find_all("td")[0].get_text(strip=True)
                if "Sunset" in row.text:
                    sunset = row.find_all("td")[0].get_text(strip=True)

        return {
            'temperature': temperature,
            'condition': condition,
            'sunrise': sunrise,
            'sunset': sunset,
            'url': url
        }
    except:
        return None
