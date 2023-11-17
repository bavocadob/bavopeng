from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_movies),
    path('genres/', views.insert_genres),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.movie_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.movie_review_detail),
]
