import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"    
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

update_graph_params = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "10.9"
}

# response = requests.post(url=update_graph_endpoint, json=update_graph_params, headers=headers)
# print(response.text)

correct_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{update_graph_params['date']}" 

correct_pixel_params = {
    "quantity": "22.3",
}

# response = requests.put(url=correct_pixel_endpoint, json=correct_pixel_params, headers=headers)
# print(response.text)

response = requests.delete(url=correct_pixel_endpoint, headers=headers)
print(response.text)