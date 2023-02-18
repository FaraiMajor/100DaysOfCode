import requests
from datetime import datetime
import smtplib
import time


url = "http://api.open-notify.org/iss-now.json"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
response.raise_for_status()
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (float(longitude), float(latitude))
print(iss_position)
