import requests
from dotenv import load_dotenv
import os 

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_COUNTRY_CODE = input("Enter your country code: ")
WEATHER_ZIP_CODE = input("Enter your zip code: ")

WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?zip={WEATHER_ZIP_CODE},{WEATHER_COUNTRY_CODE}&appid={WEATHER_API_KEY}"

result = requests.get(WEATHER_URL)

print("\nSTATUS CODE\n")
print(result.status_code)

print("\nOUTPUT\n")
print(result.json())