import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
movie_titles = soup.find_all(name="h3", class_="title")

movies_list = [movie.getText() for movie in movie_titles]
movies_list.reverse()
movies_list[11] = movies_list[11].replace(":",")")

ranks = [rank.split(")")[0] + ")" for rank in movies_list]
movies = [movie.split(")")[1] for movie in movies_list]

with open("./Day_45/100_movies_to_watch/movies.txt", "w") as file:
    for i in range(len(ranks)):
        file.write(ranks[i] + movies[i] + "\n")