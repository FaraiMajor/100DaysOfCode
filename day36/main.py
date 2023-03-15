import requests
from twilio.rest import Client
from newsapi import NewsApiClient

VIRTUAL_TWILIO_NUMBER = "+188******"
VERIFIED_NUMBER = "+1929******"

NEWS_API_KEY = "9b45c*********"
STOCK_API_KEY = "NZ*******"
TWILIO_SID = "AC61375***************"
TWILIO_AUTH_TOKEN = "5b08**********"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for value in data.values()]
yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

# find price change from prev day

price_change = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)
up_down = None
if price_change > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((price_change / float(yesterday_closing_price)) * 100)
print(f"{diff_percent}%")

if abs(diff_percent) > 5:
    api = NewsApiClient(api_key=NEWS_API_KEY)
    articles = api.get_everything(q='tesla')["articles"]
    three_articles = articles[:3]
    # print(three_articles)

# format message to be send by twilio
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nSource : {article['source']['name']}\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        print(article)
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER,
        )
    print(message.sid)
