# from django.db.models import Avg
# from movies.models import Movie
import requests
from django.conf import settings
from .models import Movie
from .utils.insert_data import update_movie, insert_movie

API_KEY = settings.API_KEY

def update_now_playing():
    BASE_URL = 'https://api.themoviedb.org/3/movie/now_playing'
     
    params = {
        'api_key': settings.API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'page': 1
    }
    
    response = requests.get(BASE_URL, params=params).json()
    movies = response['results']

    now_playing = []
    for movie in movies:
        movie_id = movie['id']
        try:
            curr_movie = Movie.objects.get(pk=movie_id)
            update_movie(curr_movie, movie_id)
        except:
            insert_movie(movie_id)
        
        now_playing.append(movie_id)
    
    print('NOW_PLAYING : ', now_playing)

    
def update_upcoming():
    BASE_URL = 'https://api.themoviedb.org/3/movie/upcoming'
     
    params = {
        'api_key': settings.API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'page': 1
    }
    
    response = requests.get(BASE_URL, params=params).json()
    movies = response['results']

    upcoming = []
    for movie in movies:
        movie_id = movie['id']
        try:
            curr_movie = Movie.objects.get(pk=movie_id)
            # update_movie(curr_movie, movie_id)
        except:
            insert_movie(movie_id)
        
        upcoming.append(movie_id)
    
    print('UPCOMING : ', upcoming)


