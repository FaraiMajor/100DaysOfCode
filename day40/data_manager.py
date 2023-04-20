from pprint import pprint
import requests
from datetime import datetime
import config


SHEETY_PRICES_ENDPOINT = config.sheety_prices_endpoint
SHEETY_USERS_ENDPOINT = config.sheety_users_endpoint
SHEETY_TOKEN = config.sheety_token


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers={"Authorization": f"Bearer {SHEETY_TOKEN}"}
            )
            pprint(response.text)

    def update_destination_price(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers={"Authorization": f"Bearer {SHEETY_TOKEN}"}
            )
            pprint(response.text)

    def get_customer_emails(self):
        headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data
