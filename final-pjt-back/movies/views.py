# from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings

from .serializers import GenreSerializer
import requests

API_KEY = settings.API_KEY

# Create your views here.
def insert_movies(request):
    # page = range(1, 501)
    BASE_URL = 'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': settings.API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'primary_release_date.gte': '2017-01-01',   # 이 날짜를 컨트롤 해서 500페이지 이상 데이터 받아오기
        'sort_by': 'primary_release_date.desc',
        'page': 1
    }
    detail_params = {
        'api_key' : settings.API_KEY,
        'language' : 'ko-KR',
        'append_to_response' : 'videos,credits,release_dates,watch/providers'
    }
    
    response = requests.get(BASE_URL, params=params).json()
    
    # 검색한 조건의 페이지 개수만큼, 페이지 1씩 올려가면서 api 요청
    for page in range(1, response['total_pages'] + 1):
        params['page'] = page

        response = requests.get(BASE_URL, params=params).json()
        
        movies = response['results']  # 해당 페이지의 영화데이터(리스트)

        for movie in movies:    # 영화 리스트를 순회
            movie_id = movie['id']  # 개별영화의 ID
            DETAIL_URL = f'https://api.themoviedb.org/3/movie/{movie_id}'
            detail_response = requests.get(DETAIL_URL, params=detail_params).json()

            return JsonResponse(detail_response)


    return JsonResponse(response)



def insert_genres(request):
    url = "https://api.themoviedb.org/3/genre/movie/list"

    params = {
        'api_key': settings.API_KEY,
        'language': 'ko-KR',
    }

    response = requests.get(url, params=params).json()
    genres = response['genres']
    
    for genre in genres:
        serializer = GenreSerializer(data=genre)
        if serializer.is_valid():
            serializer.save()

    return JsonResponse(response)