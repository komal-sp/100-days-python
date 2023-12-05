from datetime import datetime
import requests

USERNAME = "komalphadtare"
PIXELA_TOKEN = "komal98papiya99sandhya98paras2002"
GRAPH_ID = "graph1"
pixela_endpoint = " https://pixe.la/v1/users"

user_params ={
    "token": "komal98papiya99sandhya98paras2002",
    "username": "komalphadtare",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today= datetime(year=2023, month=12, day=3)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

# pixela_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(pixela_response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "12"
}
update_response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
print(update_response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)