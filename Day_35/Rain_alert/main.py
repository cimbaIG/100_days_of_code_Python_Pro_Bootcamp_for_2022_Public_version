import requests
from twilio.rest import Client
import os

OWM_Endpoint = ""
api_key = os.environ.get("OWM_API_KEY")
account_sid = ""
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 45.815,
    "lon": 15.9819,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# My solution
will_rain = False
for hour in weather_data["hourly"][:12]:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_="",
        to=""
    )
    print(message.status)