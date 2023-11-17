# from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import GenreSerializer
from .models import Genre, Movie, Actor, Director, Review
from .serializers import MovieSerializer, ReviewSerializer
import requests
import re




API_KEY = settings.API_KEY

# Create your views here.
def insert_movies(request):
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
    # for page in range(1, response['total_pages'] + 1):
    for page in range(300, 311):
        params['page'] = page

        response = requests.get(BASE_URL, params=params).json()
        
        movies = response['results']  # 해당 페이지의 영화데이터(리스트)

        for movie in movies:    # 영화 리스트를 순회
            movie_id = movie['id']  # 개별영화의 ID
            DETAIL_URL = f'https://api.themoviedb.org/3/movie/{movie_id}'
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


    return JsonResponse(response)



def insert_genres(request):
    # url = "https://api.themoviedb.org/3/genre/movie/list"

    # params = {
    #     'api_key': settings.API_KEY,
    #     'language': 'ko-KR',
    # }
    
    # response = requests.get(url, params=params).json()
    # genres = response['genres']
    genres = {
        "results" :[
        {
        "id": 28,
        "name": "액션"
        },
        {
        "id": 12,
        "name": "모험"
        },
        {
        "id": 16,
        "name": "애니메이션"
        },
        {
        "id": 35,
        "name": "코미디"
        },
        {
        "id": 80,
        "name": "범죄"
        },
        {
        "id": 99,
        "name": "다큐멘터리"
        },
        {
        "id": 18,
        "name": "드라마"
        },
        {
        "id": 10751,
        "name": "가족"
        },
        {
        "id": 14,
        "name": "판타지"
        },
        {
        "id": 36,
        "name": "역사"
        },
        {
        "id": 27,
        "name": "공포"
        },
        {
        "id": 10402,
        "name": "음악"
        },
        {
        "id": 9648,
        "name": "미스터리"
        },
        {
        "id": 10749,
        "name": "로맨스"
        },
        {
        "id": 878,
        "name": "SF"
        },
        {
        "id": 10770,
        "name": "TV 영화"
        },
        {
        "id": 53,
        "name": "스릴러"
        },
        {
        "id": 10752,
        "name": "전쟁"
        },
        {
        "id": 37,
        "name": "서부"
        }
    ]
    }
    for genre in genres['results']:
        serializer = GenreSerializer(data=genre)
        if serializer.is_valid():
            serializer.save()

    return JsonResponse(genres)



@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET','POST'])
def movie_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'POST':  # 게시글에 대한 리뷰 작성
        serializer = ReviewSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)
    elif request.method == 'GET':  # 게시글에 대한 리뷰 조회
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    

    if request.method == 'GET': # 리뷰 단일 조회
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.user and request.user.is_authenticated and request.user == review.user:  # 로그인한 리뷰 작성 유저만 접근 가능
        if request.method == 'PUT':  # 리뷰 수정
            serializer = ReviewSerializer(data=request.data, instance=review, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'DELETE':  # 리뷰 삭제
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)



