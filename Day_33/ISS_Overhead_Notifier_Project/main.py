import requests
from datetime import datetime
import smtplib

MY_LAT = 45.706299 # Your latitude
MY_LONG = 16.393641 # Your longitude
MY_EMAIL = ""
SEND_TO = ""
PASSWORD = ""
SMTP_VALUE = "smtp.gmail.com"

def send_email():
    with smtplib.SMTP(SMTP_VALUE, 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=SEND_TO, msg=f"Subject:ISS Notifier\n\nHi Mihael,\n\nlook up at the sky! The ISS is flying just above you right now!\n\nBest regards,\nYour automatic ISS Notifier.")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if (MY_LAT <= iss_latitude + 5 and MY_LAT >= iss_latitude - 5) and \
    (MY_LONG <= iss_longitude + 5 and MY_LONG >= iss_longitude - 5):
    if time_now.hour >= sunset and time_now.hour <= sunrise:
        send_email()