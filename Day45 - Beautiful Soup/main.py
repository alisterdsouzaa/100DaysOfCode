"""

Beautiful Soup is a Python library for parsing HTML and XML documents. It provides a way to extract data from
these documents, which can be useful for a variety of tasks, such as web scraping, data mining, and natural language
processing.

"""

from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf8") as html_file:
    data = html_file.read()

soup = BeautifulSoup(data, 'html.parser')
print(soup.title.string)

# all_anchor_tags = soup.findAll(name="a")
# # print(all_anchor_tags)
#
# print("\n")
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

heading = soup.findAll(name="h3", class_="heading")
print(heading)
