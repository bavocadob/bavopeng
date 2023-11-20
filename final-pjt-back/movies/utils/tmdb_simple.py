import requests


class TMDB(object):
    BASE_PATH = 'https://api.themoviedb.org/3/'

    def __init__(self, api_key):
        API_KEY = api_key
    
    def get_response(self, **kwargs):
        BASE_URL = 'https://api.themoviedb.org/3/discover/movie'
        params = {
            'api_key': self.API_KEY,
            'language': 'ko-KR',
            'region': 'KR',
        }
        for k, v in kwargs.items():
            params[k] = v
        
        response = requests.get(BASE_URL, params=params).json()

        return response