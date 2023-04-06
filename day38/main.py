import requests
from datetime import datetime
import config

GENDER = "male"
WEIGHT_KG = "85"
HEIGHT_CM = "154"
AGE = "25"

APP_ID = config.app_id
API_KEY = config.api_key
SHEETY_TOKEN = config.sheety_token

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = config.sheety_endpoint

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()  # send to sheety
print(result)

################### Add data to google sheet using Sheety######################
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for data in result["exercises"]:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
sheety_res = requests.post(sheety_endpoint, json=sheet_data, headers=headers)
print(sheety_res.text)
