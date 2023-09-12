"""
This code checks the price of an Amazon product and sends an email if the price drops below a certain threshold.
The email contains the price of the product, the link to the product page, and the subject "Amazon Prize Alert!".
"""
import smtplib
import requests
from bs4 import BeautifulSoup

email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"
amazon_product_website = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7"
}

my_desired_price = 200


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # Make sure your email providers SMTP is correct
        connection.starttls()  # Starts Transfer Layer Security
        connection.login(user=email, password=password)  # Logged in using email and password.
        connection.sendmail(from_addr=email,
                            to_addrs="alisterdsouzaa@outlook.com",
                            msg="Subject: Amazon Prize Alert!!\n\n"
                                f"Prize for the Item is dropped to {price_as_float} here is the link to buy it \n {amazon_product_website}")


response = requests.get(url=amazon_product_website, headers=headers)
if response.status_code == 200:
    print("Request Success...")
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    price = soup.find(class_="a-offscreen").get_text()
    # print(price)
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)
    if price_as_float < my_desired_price:
        send_email()

else:
    print(f"error with response code : {response.status_code}")
