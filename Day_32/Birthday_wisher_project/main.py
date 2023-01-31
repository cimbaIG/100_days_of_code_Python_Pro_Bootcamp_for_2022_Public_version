import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = ""
PASSWORD = ""
SMTP_VALUE = "smtp.gmail.com"

def pick_letter():
    rand_int = random.randint(1,3)
    with open(f"./Day_32/Birthday_wisher_project/letter_templates/letter_{rand_int}.txt", "r") as file:
        letter = file.read()
    return letter

def send_email(letter, send_to):
    with smtplib.SMTP(SMTP_VALUE, 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=send_to, msg=f"Subject:Happy birthday!\n\n{letter}.")

birthdays = pd.read_csv("./Day_32/Birthday_wisher_project/birthdays.csv")
birthdays_list = birthdays.to_dict(orient="records")

day = dt.datetime.now().day
month = dt.datetime.now().month

for birthday in birthdays_list:
    if birthday["month"] == month and \
        birthday["day"] == day:
        letter = pick_letter().replace("[NAME]", f"{birthday['name']}")
        send_email(letter=letter, send_to=birthday['email'])