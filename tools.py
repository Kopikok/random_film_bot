import json
import random
import urllib
import requests


def get_movie_info(api_key):
    movie_id = random_imdb_id()
    movie_data = download_movie_data(movie_id, api_key)
    while not movie_data:
        movie_id = random_imdb_id()
        movie_data = download_movie_data(movie_id, api_key)
    return collect_description(movie_data), get_movie_poster(movie_id, api_key)


def get_good_movie_info(api_key):
    total_score = 0
    while total_score < 4:
        movie_id = random_imdb_id()
        movie_data = download_movie_data(movie_id, api_key)
        total_score = len(movie_data) - list(movie_data.values()).count('N/A')
    return collect_description(movie_data), get_movie_poster(movie_id, api_key)


def download_movie_data(imdb_id, api_key):
    omdb_url = "http://www.omdbapi.com/"
    my_params = {'i': imdb_id, 'apikey': api_key}
    movie_data = json.loads(requests.get(url=omdb_url, params=my_params).text)
    try:
        return {'Title': movie_data['Title'],
                'Year': movie_data['Year'],
                'Genre': movie_data['Genre'],
                'imdbRating': movie_data['imdbRating'],
                'imdbVotes': movie_data['imdbVotes'],
                'Plot': movie_data['Plot']}
    except KeyError:
        return None


def collect_description(movie_data):
    description = (f"{movie_data['Title']} ({movie_data['Year']})" +
                   f"\nGenres: {movie_data['Genre']}")
    if movie_data['imdbRating'] != 'N/A':
        description += f"\nIMDB rating: {movie_data['imdbRating']} / 10"
        if movie_data['imdbVotes'] != 'N/A':
            description += f"(based on {movie_data['imdbVotes']} votes)"
    if movie_data['Plot'] != 'N/A':
        description += f"\n{movie_data['Plot']}"
    return description


def get_movie_poster(imdb_id, api_key):
    url = f"http://img.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        no_poster_pic = open("data/no_poster.jpg", "rb")
        return no_poster_pic


def random_imdb_id():
    with open("data/titles_dataset.ds") as my_file:
        return random.choice(my_file.readline().split())
