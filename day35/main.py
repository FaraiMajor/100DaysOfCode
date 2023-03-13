import requests


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
    print("It's going to rain today. Remember to bring an ☔️")
