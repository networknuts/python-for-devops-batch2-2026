import requests
from dotenv import load_dotenv
import os 
import sys 

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_COUNTRY_CODE = input("Enter your country code: ")
WEATHER_ZIP_CODE = input("Enter your zip code: ")

WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?zip={WEATHER_ZIP_CODE},{WEATHER_COUNTRY_CODE}&appid={WEATHER_API_KEY}"

result = requests.get(WEATHER_URL)

if result.status_code == 200: #200 status code is a successful connection
    print("Connected successfully, fetching information")
    print("="*40)
    print(result.json())
else:
    print("Error: Something went wrong.")
    sys.exit(1)