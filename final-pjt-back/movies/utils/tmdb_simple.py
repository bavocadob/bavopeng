import requests


class TMDB(object):
    BASE_PATH = 'https://api.themoviedb.org/3/'

    def __init__(self, api_key):
        API_KEY = api_key