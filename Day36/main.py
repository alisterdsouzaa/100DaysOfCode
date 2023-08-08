__author__ = "Alister D'souza"
__copyright__ = " Copyright (C) 2007 Free Software Foundation, Inc."
__credits__ = " Stack Overflow "
__license__ = "GNU"
__version__ = "1.0.1"
__maintainer__ = "Alister D'souza"
__email__ = "alisterdsouzaa@outlook.com"
__status__ = "Release"

from datetime import date, timedelta
from twilio.rest import Client
import os
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
VIRTUAL_TWILIO_NUMBER = ""
VERIFIED_NUMBER = ""

today = date.today()
yesterday = today - timedelta(days=1)
print(today)
print(yesterday)

STOCK_DATA_API_KEY = os.getenv("API_KEY", default="No Environment Key found")
STOCK_NEWS_DATA_API_KEY = ""

#  Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]

paramaters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_DATA_API_KEY,
    # "datatype": "csv"
}

response = requests.get(url=STOCK_ENDPOINT, params=paramaters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
# print(stock_data_list)

yesterday_data = stock_data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]
print(yesterdays_closing_price)

# Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#  Get the day before yesterday's closing stock price
day_before_yesterdays_data = stock_data_list[1]
day_before_yesterdays_closing_price = day_before_yesterdays_data["4. close"]
print(day_before_yesterdays_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterdays_closing_price) - float(day_before_yesterdays_closing_price))
print(difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_difference = (difference / float(yesterdays_closing_price)) * 100
print(percentage_difference)

## STEP 2: https://newsapi.org/
# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

if percentage_difference >= 0.8:
    news_api_parameters = {
        "apiKey": STOCK_NEWS_DATA_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_api_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    print(articles)
    first_3_articles = articles[:3]
    print(first_3_articles)

    # a = first_3_articles[0]["title"]
    # print(a)
    # a = first_3_articles[0]["description"]
    # print(a)
    #

    #Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.
    # Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"Headline: {article['title']}.\nBrief:{article['description']}"
                          for article in first_3_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
