from django.urls import path
from . import views

urlpatterns = [
    path('movie/search/<str:query>/', views.movie_search),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('movie/<int:movie_pk>/like/', views.movie_like),
    path('movie/<int:movie_pk>/dislike/', views.movie_dislike),
    path('movie/<int:movie_pk>/reviews/', views.movie_review),
    path('movie/<int:movie_pk>/reviews/<int:page>/', views.movie_review_pages),

    path('review/<int:review_pk>/', views.movie_review_detail),
    path('review/<int:review_pk>/like/', views.movie_review_like),

    path('recommends/movie/', views.recommend_by_movies),
]
