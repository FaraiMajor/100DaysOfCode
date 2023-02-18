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

print(data)
