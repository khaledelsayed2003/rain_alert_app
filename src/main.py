import requests
from dotenv import load_dotenv
import os


# Load the .env file from the config folder
load_dotenv("rain_alert_app/config/.env")

MY_OWN_API_KEY = os.getenv("WEATHER_API_KEY")
