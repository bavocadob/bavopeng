from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
import django
django.setup()

from movies.models import Movie, Actor, Director, Genre, WatchProvider
from movies.serializers import GenreSerializer

import requests
import re


API_KEY = settings.API_KEY


def insert_movies():
    


    BASE_URL = 'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': settings.API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'primary_release_date.lte': '2000-01-01',   # 이 날짜를 컨트롤 해서 500페이지 이상 데이터 받아오기
        'primary_release_date.gte': '1960-01-01',   # 이 날짜를 컨트롤 해서 500페이지 이상 데이터 받아오기
        'sort_by': 'primary_release_date.desc',
        'page': 1
    }
    
    response = requests.get(BASE_URL, params=params).json()
    
    # 검색한 조건의 페이지 개수만큼, 페이지 1씩 올려가면서 api 요청
    # for page in range(1, response['total_pages'] + 1):
    for page in range(1, response['total_pages'] + 1):
        params['page'] = page

        response = requests.get(BASE_URL, params=params).json()
        
        movies = response['results']  # 해당 페이지의 영화데이터(리스트)

        for movie in movies:    # 영화 리스트를 순회
            movie_id = movie['id']  # 개별영화의 ID
            if Movie.objects.filter(id=movie_id).exists():
                continue
            
            insert_movie(movie_id)


def insert_watch_providers():
    watch_providers = [
        { 
            'id': 8,
            'name': '넷플릭스',
            'url': 'https://www.netflix.com/kr/',
            'logo_img': '/t2yyOv40HZeVlLjYsCsPHnWLk4W.jpg',
        },
        { 
            'id': 97,
            'name': '왓챠',
            'url': 'https://watcha.com/',
            'logo_img': '/vXXZx0aWQtDv2klvObNugm4dQMN.jpg',
        },
        { 
            'id': 337,
            'name': '디즈니 플러스',
            'url': 'https://www.disneyplus.com/ko-kr',
            'logo_img': '/7rwgEs15tFwyR9NPQ5vpzxTj19Q.jpg',
        },
   ]
    for provider in watch_providers:
        watch_provider = WatchProvider.objects.create(**provider)
        watch_provider.save()


def insert_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list"

    params = {
        'api_key': settings.API_KEY,
        'language': 'ko-KR',
    }
    
    response = requests.get(url, params=params).json()
    genres = response['genres']

    for genre in genres['results']:
        serializer = GenreSerializer(data=genre)
        if serializer.is_valid():
            serializer.save()


def insert_movie(movie_id):
    def get_trailer(response):
        videos = response['videos']
        if videos:
            for video in videos['results']:
                video_type = video['type'].lower()
                if video_type == 'trailer' or video_type == 'teaser':
                    return video['key']
        return ''
    
    def get_certification(response):
        release_dates = response['release_dates']['results']
        for release_date in release_dates:
            if release_date['iso_3166_1'] == 'KR':
                return release_date['release_dates'][-1]['certification']
        return ''

    def add_genres(movie_obj, genres):
        for genre_data in genres:
            try:
                # Genre 객체를 가져오거나 생성
                genre = Genre.objects.get(id=genre_data["id"])
            except ObjectDoesNotExist:
                genre = Genre.objects.create(**genre_data)
            # Movie 객체의 genres 필드에 추가
            movie_obj.genres.add(genre)


    def create_people(actor_id, type):
        ACTOR_DETAIL_URL = f'https://api.themoviedb.org/3/person/{actor_id}'
        actor_params = {
            'api_key' : settings.API_KEY,
            'language' : 'ko-KR'
        }
        response = requests.get(ACTOR_DETAIL_URL, params=actor_params).json()
        
        people_fields = {k: v for k, v in response.items() if k in [f.name for f in Actor._meta.get_fields()]}
        people_fields['korean_name'] = ''
        if people_fields['profile_path'] is None:
            people_fields['profile_path'] = ''

        for aka in response['also_known_as']:
            if re.search("[가-힣]", aka):
                people_fields['korean_name'] = aka
                break
        
        if type == 'actor':
            people_obj = Actor.objects.create(**people_fields)
        elif type == 'director':
            people_obj = Director.objects.create(**people_fields)

        return people_obj


    def add_actors(movie_obj, cast):
        for i in range(min(10, len(cast))):
            cast_actor = cast[i]
            try:
                actor = Actor.objects.get(id=cast_actor['id'])
            except ObjectDoesNotExist:
                actor = create_people(cast_actor['id'], 'actor')
            movie_obj.actors.add(actor)

    def add_directors(movie_obj, crews):
        for crew in crews:
            if crew['job'].lower() != 'director':
                continue
            try:
                director = Director.objects.get(id=crew['id'])
            except ObjectDoesNotExist:
                director = create_people(crew['id'], 'director')
            movie_obj.directors.add(director)

    def add_providers(movie_obj, providers:dict):
        flatrates = providers.setdefault('KR', dict()).setdefault('flatrate', dict())
        if not flatrates:
            return
        
        for flatrate in flatrates:
            try:
                watch_provider = WatchProvider.objects.get(pk=flatrate['provider_id'])
                movie_obj.watch_providers.add(watch_provider)
            except ObjectDoesNotExist:
                continue

    detail_params = {
        'api_key' : settings.API_KEY,
        'language' : 'ko-KR',
        'append_to_response' : 'videos,credits,release_dates,watch/providers'
    }
    
    DETAIL_URL = f'https://api.themoviedb.org/3/movie/{movie_id}'
    try:
        detail_response = requests.get(DETAIL_URL, params=detail_params).json()

        movie_fields = {k: v for k, v in detail_response.items() if k in [f.name for f in Movie._meta.get_fields() if not isinstance(f, models.ManyToManyField)]}
        movie_fields['trailer'] = get_trailer(detail_response)
        movie_fields['certification'] = get_certification(detail_response)
        if movie_fields['backdrop_path'] is None:
            movie_fields['backdrop_path'] = ''

        if movie_fields['poster_path'] is None:
            movie_fields['poster_path'] = ''

        movie_obj = Movie.objects.create(**movie_fields)

        add_genres(movie_obj, detail_response['genres'])
        add_actors(movie_obj, detail_response['credits']['cast'])
        add_directors(movie_obj, detail_response['credits']['crew'])
        add_providers(movie_obj, detail_response['watch/providers']['results'])
    except:
        print(movie_id)


def update_movie(movie, movie_id):
    def get_trailer(response):
        videos = response['videos']
        if videos:
            for video in videos['results']:
                video_type = video['type'].lower()
                if video_type == 'trailer' or video_type == 'teaser':
                    return video['key']
        return ''
    
    def get_certification(response):
        release_dates = response['release_dates']['results']
        for release_date in release_dates:
            if release_date['iso_3166_1'] == 'KR':
                return release_date['release_dates'][-1]['certification']
        return ''

    detail_params = {
        'api_key' : settings.API_KEY,
        'language' : 'ko-KR',
        'append_to_response' : 'videos,credits,release_dates,watch/providers'
    }
    
    DETAIL_URL = f'https://api.themoviedb.org/3/movie/{movie_id}'

    try:
        detail_response = requests.get(DETAIL_URL, params=detail_params).json()

        movie_fields = {k: v for k, v in detail_response.items() if k in [f.name for f in Movie._meta.get_fields() if not isinstance(f, models.ManyToManyField)]}
        movie_fields['trailer'] = get_trailer(detail_response)
        movie_fields['certification'] = get_certification(detail_response)
        if movie_fields['backdrop_path'] is None:
            movie_fields['backdrop_path'] = ''

        if movie_fields['poster_path'] is None:
            movie_fields['poster_path'] = ''

        for key, value in movie_fields.items():
            setattr(movie, key, value)
        movie.save()

    except:
        print(movie_id)