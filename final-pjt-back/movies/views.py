from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, MovieListSerializer
from .models import Genre, Movie, Actor, Director, Review, WatchProvider, NowShowing, Upcoming


API_KEY = settings.API_KEY


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET','POST'])
def movie_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.user.is_authenticated and request.method == 'POST':  # 영화에 대한 리뷰 작성
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)
    elif request.method == 'GET':  # 영화에 대한 리뷰 조회
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_search(request, query):
    query_no_space = query.replace(' ', '')
    movies = Movie.objects.all().order_by('-rating_cnt')
    filtered_movies = list(filter(lambda movie: query_no_space.lower() in movie.title.lower().replace(' ', '') or query_no_space.lower() in movie.original_title.lower().replace(' ', ''), movies))[:10]
    serializer = MovieListSerializer(filtered_movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    
    if request.method == 'POST':
        if movie.liked_by.filter(pk=user.pk).exists():
            movie.liked_by.remove(user)
        else:
            if movie.disliked_by.filter(pk=user.pk).exists():
                movie.disliked_by.remove(user)
            movie.liked_by.add(user)
        return Response(status=status.HTTP_200_OK)

            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_dislike(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if request.method == 'POST':
        if movie.disliked_by.filter(pk=user.pk).exists():
            movie.disliked_by.remove(user)
        else:
            movie.liked_users.add(user)
        return Response(status=status.HTTP_200_OK)            


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_wish(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if request.method == 'POST':
        if movie.wished_by.filter(pk=user.pk).exists():
            movie.wished_by.remove(user)
        else:
            movie.wished_by.add(user)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def movie_review_detail(request, review_pk):
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
    

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_review_pages(request, movie_pk, page):
    PAGE_SIZE = 10
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 정렬 방식을 URL 쿼리 파라미터에서 가져옵니다.
    # 기본값은 1입니다.
    sort_by = int(request.GET.get('sort_by', 1))
    
    # 정렬 방식에 따른 필드 이름을 매핑하는 딕셔너리를 생성합니다.
    sort_mapping = {
        1: 'created_at',
        2: '-created_at',
        3: 'rating',
        4: '-rating'
    }

    sort_field = sort_mapping.get(sort_by, 'created_at')
    reviews = movie.review_set.all().order_by(sort_field)

    paginator = Paginator(reviews, PAGE_SIZE)
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    serializer = ReviewSerializer(reviews, many=True)
    
    return Response({
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': min(page, paginator.num_pages),
        'results': serializer.data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
 
    if request.method == 'POST':
        if review.liked_by.filter(pk=user.pk).exists():
            review.liked_by.remove(user)
        else:
            review.liked_by.add(user)
        
        result = {
            'like_cnt' : review.liked_by.count(),
            'is_like' : review.liked_by.filter(pk=user.pk).exists()
        }
        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_by_movies(request):
    # user = request.user
    # reviews = user.review_set.filter(rating__gte=7)
    # recommend = { 'movie_list' : [] }

    # RECOMMEND_URL = 'https://api.themoviedb.org/3/movie/520951/recommendations?language=ko-KR&page=1'
    # for review in reviews:
    #     params = {
            
    #     }
         
    #     movie_id = review.movie_id
    #     recommend['movie_list'].append(movie_id)

    # result = { 'results' : recommend }
    # return Response(result)
    pass
    

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_nowshowing(request):
    now_showing = NowShowing.objects.all()
    movies = [ns.movie for ns in now_showing if ns.movie.poster_path]
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_upcoming(request):
    upcoming = Upcoming.objects.all()
    movies = [ns.movie for ns in upcoming if ns.movie.poster_path]
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)