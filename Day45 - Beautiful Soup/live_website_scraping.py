import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.chara.co.in/")
print(response)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
print(soup.title)

all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)

print("\n")

for tag in all_anchor_tags:
    print(tag.get("href"))
