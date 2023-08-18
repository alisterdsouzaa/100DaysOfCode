import requests
import datetime

QUANTITY = str(input("Enter number of KMs you ran today?"))

date = str(datetime.date.today()).split("-")
today = ""
for _ in date:
    today += _
print(today)


USERNAME = "alisterdsouzaa13"
TOKEN = "alister@tokenID"

pixela_api_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "alister@tokenID",
    "username": "alisterdsouzaa13",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_api_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_api_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":"graph1",
    "name":"Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/graph1"

post_params = {
    "date": today,
    "quantity": QUANTITY
}

# response = requests.post(url=post_endpoint, json=post_params, headers=headers)
# print(response.text)

# update_endpoint = f"{pixela_api_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_api_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
