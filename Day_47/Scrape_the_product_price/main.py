import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Apple-MacBook-13-inch-Storage-Keyboard/dp/B08FG7S7G7/ref=sr_1_5?keywords=macbook+pro&qid=1652044047&sprefix=macbook%2Caps%2C190&sr=8-5"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = ""
MY_PASSWORD = ""
SET_PRICE = 750

def send_email(product, price):
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="",
                    msg=f"Subject:Low Price at Amazon!\n\nDear Mihael,\n\nproduct {product} is now at low price - only {price}!"
        )

headers = {
    "Accept-Language": "hr-HR,hr;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name="span", class_="a-offscreen")
price = float(price.text.split('$')[1])

product = soup.find(name="span", id="productTitle").text.strip()

if price <= SET_PRICE:
    send_email(product=product, price=price)