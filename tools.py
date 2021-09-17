import json
import random
import urllib
import requests


def get_movie_info(imdb_id: str, api_key: str) -> str:
    omdb_url = "http://www.omdbapi.com/"
    my_params = {'i': imdb_id, 'apikey': api_key}
    movie_data = json.loads(requests.get(url=omdb_url, params=my_params).text)
    description = (f"{movie_data['Title']} ({movie_data['Year']})" +
                   f"\nGenres: {movie_data['Genre']}")

    if movie_data['imdbRating'] != 'N/A':
        description += f"\nIMDB rating: {movie_data['imdbRating']} / 10"
    if movie_data['imdbVotes'] != 'N/A':
        description += f"(based on {movie_data['imdbVotes']} votes)"
    if movie_data['Plot'] != 'N/A':
        description += f"\n\n{movie_data['Plot']}"
    return description


def get_movie_poster(imdb_id: str, api_key: str):
    url = f"http://img.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        no_poster_pic = open("data/no_poster.jpg", "rb")
        return no_poster_pic


def random_imdb_id():
    with open("data/titles_dataset.ds") as my_file:
        return random.choice(my_file.readline().split())
