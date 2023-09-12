import re
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
SECRET_CODE = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=SECRET_CODE,
        show_dialog=True,
        cache_path="token.txt"
    )
)


def validate_date(date):
    regex = r"^\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$"
    if re.match(regex, date):
        return True
    else:
        return False


date = input("Which year do you want to travel to? Enter a date in the format YYYY-MM-DD: ")

if validate_date(date):
    print("The date is valid.")
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    if response.status_code == 200:
        print("Getting response form website...")
        webpage = response.text
        soup = BeautifulSoup(webpage, "html.parser")
        song_names_spans = soup.select("li ul li h3")
        # print(song_names_spans)
        song_names = [song.getText().strip() for song in song_names_spans]
        print(song_names)

        user_id = sp.current_user()["id"]
        print(user_id)
else:
    print("The date is not valid.")
