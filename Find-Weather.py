"""
# Do it for a specific city 

import requests
from bs4 import BeautifulSoup

city = input("Enter the city name: ")
city_formatted = city.lower().replace(" ", "-")

url = f"https://www.timeanddate.com/weather/usa/{city_formatted}"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

try:
    # Get temperature
    temperature = soup.find("div", class_="h2").get_text(strip=True)
    
    # Get condition (usually under <p> tag with class "bk-focus__qlook")
    condition_div = soup.find("div", class_="bk-focus__qlook")
    condition = condition_div.find("p").get_text(strip=True)

    print(f"Weather in {city.title()}:")
    print(f"Temperature: {temperature}")
    print(f"Condition: {condition}")

except AttributeError:
    print("City not found or website structure changed. Please check the city name and try again.")
"""

# Do it for multiple cities

import requests
from bs4 import BeautifulSoup

def format_location(name):
    return name.lower().strip().replace(" ", "-")

# Input from user
country = input("Enter the country name: ")
city = input("Enter the city name: ")

country_formatted = format_location(country)
city_formatted = format_location(city)

url = f"https://www.timeanddate.com/weather/{country_formatted}/{city_formatted}"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        # Get temperature
        temperature = soup.find("div", class_="h2").get_text(strip=True)

        # Get weather condition
        condition_div = soup.find("div", class_="bk-focus__qlook")
        condition = condition_div.find("p").get_text(strip=True)

        print(f"\nWeather in {city.title()}, {country.title()}:")
        print(f"Temperature: {temperature}")
        print(f"Condition: {condition}")

    except AttributeError:
        print("\nCould not extract weather data. The website's structure may have changed.")
else:
    print("\nCity or country not found. Please check the names and try again.")
