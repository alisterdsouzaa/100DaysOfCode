"""
This code scrapes the top 100 movies from the website empireonline.com.

Author: alisterdsouzaa

"""
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
print(response.status_code)

webpage = response.text

"""
Data to scrape is in h3 tag
<h3 class="listicleItem_listicle-item__title__hW_Kn">98) Paddington 2</h3>
"""

soup = BeautifulSoup(webpage, "html.parser")

all_movies = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
# print(all_movies)

movie_titles = [titles.getText() for titles in all_movies]
print(movie_titles)

movie_titles = movie_titles[::-1]
print(movie_titles)

with open("top_100_movies.txt", "w") as file:
    for movie_title in movie_titles:
        file.writelines(movie_title)
        file.write("\n")
