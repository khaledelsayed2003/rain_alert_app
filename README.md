# 🌧️ Rain Alert App (OpenWeatherMap + Twilio)

A small Python project that checks the weather forecast using the **OpenWeatherMap API** and sends an **SMS alert** via **Twilio** if rain is expected in the next few hours.

This project was built for learning purposes: APIs, environment variables, and basic automation.

---

## ✨ Features

- Fetches 3-hour forecast data from **OpenWeatherMap**
- Checks several upcoming time slots (e.g. next **12 hours**)
- Detects rain/snow/drizzle/thunderstorm based on weather condition codes
- Sends an SMS like:

> ☔ Rain is expected soon. Please bring an umbrella, Mr. Khaled.

- Uses **environment variables** for all secrets (API keys, tokens, phone number)

---

## 🧰 Tech Stack

- **Python 3.10+**
- [requests](https://pypi.org/project/requests/) – for HTTP requests
- [python-dotenv](https://pypi.org/project/python-dotenv/) – for loading `.env` file
- [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)

---

## 🔐 Environment Variables

All secrets are stored in config/.env (which is ignored by git).

I used config/.env.example as a template. The .env file should define:

- WEATHER_API_KEY=your_openweathermap_api_key
- TWILIO_ACCOUNT_SID=your_twilio_account_sid
- TWILIO_AUTH_TOKEN=your_twilio_auth_token
- PHONE_NUMBER=your_real_phone_number_in_e164_format   # e.g. +905xxxxxxxxx

---


## 🛠 Installation & Setup

- 1. Clone the repo
    - git clone https://github.com/khaledelsayed2003/rain_alert_app.git
    - cd rain_alert_app


- 2. Create and activate a virtual environment (recommended)
    - python -m venv .venv
    - ## Windows:
      - .venv\Scripts\activate
    - ## macOS / Linux:
      - source .venv/bin/activate


- 3. Install dependencies
    - pip install -r requirements.txt


- 4. Create your .env file
    - copy config\.env.example config\.env      # Windows
    -  ## or
    - cp config/.env.example config/.env        # macOS / Linux
    
       - Then open config/.env and fill in your real values:

            - WEATHER_API_KEY – from OpenWeatherMap

            - TWILIO_ACCOUNT_SID – from your Twilio console

            - TWILIO_AUTH_TOKEN – from your Twilio console

            - PHONE_NUMBER – the phone number that will receive the SMS



- 5. Configure Twilio trial number
    - Make sure your Twilio trial phone number is allowed to send SMS to your PHONE_NUMBER.
    - In src/main.py, the from_ field must be your Twilio number, for example:
        - message = client.messages.create(
            - body="☔ Rain is expected soon. Please bring an umbrella, Mr. Khaled.",
            - from_="+1xxxxxxxxxx",   # your Twilio number
            - to=phone_number,
        - )


---

## ⚙️ Customization

- You can easily change:

   - Location – update the latitude/longitude in main.py:
        - MY_LAT = 40.991309
        - MY_LONG = 28.771965

   - Forecast horizon – how many 3-hour periods to check:
        - forecast_count = 4  # 4 x 3h = next 12 hours

   - Alert message – edit the body parameter in client.messages.create(...).

---

## 📄 License

- This project is licensed under the MIT License.
- Feel free to use, modify, and learn from it.

---

## 💫 Author
Khaled Elsayed (KE)
Developed as part of a Python learning.

---


## 📁 Project Structure
```bash
rain_alert_app/
├─ config/
│  ├─ .env              # real secrets (NOT committed)
│  └─ .env.example      # template with variable names only
├─ src/
│  ├─ main.py           # main script (rain check + SMS send)
│  └─ assets/
│     └─ images/
│        ├─ sms_rain_alert_conversation.png
│        └─ sms_rain_alert_notification.png
├─ .gitignore
├─ LICENSE
├── README.md
└─ requirements.txt


