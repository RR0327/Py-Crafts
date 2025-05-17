import requests
from bs4 import BeautifulSoup

country = input("Enter the country: ").lower().replace(" ", "-")
city = input("Enter the city: ").lower().replace(" ", "-")

url = f"https://www.timeanddate.com/weather/{country}/{city}"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

try:
    temperature = soup.find('div', class_='h2').get_text(strip=True)
    weather_description = soup.find('div', class_='h2').find_next('p').get_text(strip=True)

    print(f"\nWeather in {city.title()}, {country.title()}:")
    print(f"Temperature: {temperature}")
    print(f"Description: {weather_description}")

except AttributeError:
    print("City or country not found. Please check the inputs and try again.")
