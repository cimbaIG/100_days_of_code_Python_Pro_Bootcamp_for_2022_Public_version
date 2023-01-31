import datetime as dt
import smtplib
import random

MY_EMAIL = ""
PASSWORD = ""
SMTP_VALUE = ""
SEND_TO = ""

def pick_a_quote():
    with open("./Day_32/Birthday_wisher_project/quotes.txt") as file:
        quote_list = file.readlines()
        quote = random.choice(quote_list)
    return quote

def send_email():
    with smtplib.SMTP(SMTP_VALUE, 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=SEND_TO, msg=f"Subject:Your's today motivational quote\n\n{pick_a_quote()}.")

if dt.datetime.now().weekday() == 2:
    send_email()