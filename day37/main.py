import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "sdftkh45ns7j5gu"
USERNAME = "faraimajor"
GRAPH_ID = "graph1"

# ----------------------------CREATE PIXEL ACCOUNT------------------
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create my user account and token for future use
response = requests.post(url=pixela_endpoint, json=user_params)

print(response.text)

# ----------------------------CREATE PIXEL GRAPH------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)

# ----------------------------INPUT PIXEL GRAPH DATA------------------
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today_date = datetime.now()

pixel_data = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": input("How many Km did you run today?"),
}

response = requests.post(url=pixel_creation_endpoint,
                         json=pixel_data, headers=headers)
print(response.text)

# ----------------------------UPDATE PIXEL GRAPH DATA------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4"
}

# PUT
response = requests.put(url=update_endpoint,
                        json=new_pixel_data, headers=headers)
print(response.text)

# ----------------------------DELETE PIXEL GRAPH DATA------------------
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime('%Y%m%d')}"


# DELETE
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
