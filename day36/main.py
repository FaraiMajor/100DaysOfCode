import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+18886080561"
VERIFIED_NUMBER = "+19293369612"

NEWS_API_KEY = "9b45c3fa0be4412ca0827eb58fa5a113"
STOCK_API_KEY = "NZGT6QUSH2EOOJ02"
TWILIO_SID = "AC6137534b9baf3086289be51dccd53968"
TWILIO_AUTH_TOKEN = "3aa80206ce3438788228005c22def8e7"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, stock_params)

data = response.json()
print(data)
