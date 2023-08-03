# Learning API endpoints and parameters.
# With using this project we can sopt the ISS ( Space Center ) in the sky.
# This project will send an email where the ISS is the loction, provide by us in the lon and lat co-ordinates.
import requests
from datetime import datetime
import smtplib
import time

email = "abc@gmail.com"
password = "password"

MY_LAT = 12.971599
MY_LONG = 77.594566

def is_it_night():
    # Default Paramaters to send to API Endpoint
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().time().hour
    if sunset <= time_now <= sunrise:
        return True




def is_over_my_loc():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # raise any exception if there is any error
    response.raise_for_status()
    # getting data of JSON format in data variable
    data = response.json()
    # Extracting values from Dictionary
    iss_lattitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lattitude >= MY_LAT+5 and MY_LONG-5 <= iss_longitude >= MY_LONG+5:
        return True


while True:
    time.sleep(60)
    if is_over_my_loc() and is_it_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:  # Make sure your email providers SMTP is correct
            connection.starttls()  # Starts Transfer Layer Security
            connection.login(user=email, password=password)  # Logged in using email and password.
            connection.sendmail(from_addr=email,
                                to_addrs="receipent@abc.com",
                                msg="Subject: Iss is over your head.\n\n"
                                    "You can now watch it using a telescope")
