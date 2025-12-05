import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client


# Load the .env file from the config folder
load_dotenv("rain_alert_app/config/.env")
MY_OWN_API_KEY = os.getenv("WEATHER_API_KEY")

# Load your own Account SID and Auth Token from the .env file.
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)


# This latitude and longitude is for Istanbul City.
MY_LAT = 40.991309
MY_LONG = 28.771965

# Number of 3-hour forecast intervals to retrieve (4 intervals ≈ 12 hours)
forecast_count = 4

# Load my real phone number from the .env file.
phone_number = os.getenv("PHONE_NUMBER")
    
parameters = {
    "lat": MY_LAT, 
    "lon": MY_LONG,
    "appid": MY_OWN_API_KEY, 
    "cnt": forecast_count
}

forecast_3h_response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
forecast_3h_response.raise_for_status()
weather_data = forecast_3h_response.json()


# Check each 3-hour interval, but notify only once if any forecast predicts rain
for iteration in range(forecast_count):
    weather_id = weather_data["list"][iteration]["weather"][0]["id"]
    if int(weather_id) < 700: # Weather codes <700 = rain/snow/drizzle/thunderstorm
        message = client.messages.create(
            body="☔ Rain is expected soon. Please bring an umbrella, Mr. Khaled.",
            from_="+16105107634",
            to=phone_number,
        )
        break # Stop checking further forecasts to avoid repeated notifications
    

        