import requests

USERNAME = "alisterdsouzaa13"
TOKEN = "alister@tokenID"

pixela_api_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"f{pixela_api_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": "alister@tokenID",
    "username": "alisterdsouzaa13",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_api_endpoint,json=user_params)
# print(response.text)
