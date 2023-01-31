from pprint import pprint
import re
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
SPOTIFY_REDIRECT_URL = ""

#year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = "2000-08-12"
URL = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

top_one_song_span = soup.find_all("a", class_="c-title__link lrv-a-unstyle-link")
top_one_singer_span = soup.find_all("p", class_="c-tagline a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150")

top_one_song = [top.getText() for top in top_one_song_span]
top_one_singer = [top.getText() for top in top_one_singer_span]

song_spans = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
singer_spans = soup.find_all("span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

songs = [song.getText() for song in song_spans]
singers = [song_name.getText() for song_name in singer_spans]
songs.insert(0,top_one_song[0])
singers.insert(0,singers[0])

#Get rid of tabs and new lines in the list strings
songs = [re.sub(r"[\n\t]+", "", song) for song in songs]
singers = [re.sub(r"[\n\t]+", "", singer) for singer in singers]

#Authenticate to Spotify using spotipy library
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT_URL,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

SPOTIFY_ENDPOINT = f"https://api.spotify.com/v1/users/{user_id}/playlists"

#Searching Spotify for songs by title
song_uris = []
year = year.split("-")[0]
print(songs[0])
result = sp.search(q=f"track:{songs[0]} artist:{singers[0]} year:{year}", type="track")
print(result)
uri = result["tracks"]["items"][0]["uri"]
print(uri)
# for song in songs:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)