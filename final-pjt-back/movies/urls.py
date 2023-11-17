from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_movies),
    path('genres/', views.insert_genres),
    path('providers/', views.insert_watch_providers),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/dislike/', views.movie_dislike),
    path('<int:movie_pk>/reviews/', views.movie_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.movie_review_detail),
    path('<int:movie_pk>/reviews/<int:review_pk>/like/', views.movie_review_like),

]
