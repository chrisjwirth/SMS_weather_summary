import os
from twilio.rest import Client
import requests

# Open Weather Map
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ["OWM_API_KEY"]

# Twilio
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

params = {
    "lat": 39.69302,
    "lon": -104.88477,
    "units": "imperial",
    "exclude": "current,minutely",
    "appid": api_key
}

response = requests.get(ENDPOINT, params=params)
response.raise_for_status()

all_data = response.json()

# Tomorrow's Forecast Data
data_tomorrow = all_data["daily"][1]

description = data_tomorrow["weather"][0]["description"]
description = description.title()

chance_of_precipitation = data_tomorrow["pop"]
chance_of_precipitation = f"{int(chance_of_precipitation * 100)}%"

feels_like_morning = data_tomorrow["feels_like"]["morn"]
feels_like_morning = f"{int(feels_like_morning)}°F"

feels_like_day = data_tomorrow["feels_like"]["day"]
feels_like_day = f"{int(feels_like_day)}°F"

feels_like_evening = data_tomorrow["feels_like"]["eve"]
feels_like_evening = f"{int(feels_like_evening)}°F"

feels_like_night = data_tomorrow["feels_like"]["night"]
feels_like_night = f"{int(feels_like_night)}°F"

message_body = f"""
***Tomorrow's Weather***

Description: {description}

Chance of Precipitation: {chance_of_precipitation}

Feels Like Temp (Morning): {feels_like_morning}

Feels Like Temp (Day): {feels_like_day}

Feels Like Temp (Evening): {feels_like_evening}

Feels Like Temp (Night): {feels_like_night}
"""

phone_numbers = ['+18137317129', '+16094104124']
for phone_number in phone_numbers:
    message = client.messages \
                    .create(
                         body=message_body,
                         from_='+12627472635',
                         to=phone_number
                     )
