import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "******************"
auth_token = "******************"
api_key = "7df7c4df02edd6021c39f04315142c70"
url = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": 40.679459,
    "lon": -73.846413,
    "appid": api_key,
    "units": "imperial",
    "exclude": "current,minute,daily"
}
response = requests.request("GET", url, params=params)
response.raise_for_status()

weather_data = response.json()
weather_hourly = weather_data["hourly"]
# [:12]

will_rain = False

for hourly_data in weather_hourly[:12]:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    #  http_client=proxy_client

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+*********",
        to="+*********"
    )
print(message.sid)
