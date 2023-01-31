import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = ""
NEWS_ENDPOINT = ""

# Keys are not given due to the security reason
stock_api_key = ""
news_api_key = ""
account_sid = ""
auth_token = ""

def send_message(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body=message,
    from_="",
    to=""
    )
    print(message.status)

todays_date = dt.datetime.now().date()

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_api_key
}

news_params = {
    "q": COMPANY_NAME,
    "from": todays_date,
    "language": "en",
    "apiKey": news_api_key
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = list(stock_response.json()["Time Series (Daily)"].items())[:2]
yesterday_price = float(stock_data[0][1]["4. close"])
day_before_yesterday_price = float(stock_data[1][1]["4. close"])
diff = round(100 * (yesterday_price / day_before_yesterday_price - 1), 2)

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"][:3]

for news in news_data:
    if diff <= 0:
        message = f"🔻{diff}%" + f"\nHeadline: {news['title']}\nBrief: {news['description']}"
        send_message(message)
    if diff >= 5:
        message = f"🔺{diff}%" + f"\nHeadline: {news['title']}\nBrief: {news['description']}"
        send_message(message)