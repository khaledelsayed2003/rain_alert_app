import requests
from dotenv import load_dotenv
import os


# Load the .env file from the config folder
load_dotenv("rain_alert_app/config/.env")
MY_OWN_API_KEY = os.getenv("WEATHER_API_KEY")

# This latitude and longitude is for Istanbul City.
MY_LAT = 41.013000
MY_LONG = 28.974800 
    
parameters = {
    "lat": MY_LAT, 
    "lon": MY_LONG,
    "appid": MY_OWN_API_KEY, 
    "cnt": 4
}

forecast_3h_response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
forecast_3h_response.raise_for_status()
weather_data = forecast_3h_response.json()
print(weather_data)