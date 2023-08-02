import requests

# requesting data by passing API Endpoint, and obtaining response
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# raise any exception if there is any error
response.raise_for_status()

# getting data of JSON format in data variable
data = response.json()
print(data)

# Extracting values from Dictionary
lattitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

# Tuple of iss location data
iss_location = (lattitude,longitude)
print(iss_location)
