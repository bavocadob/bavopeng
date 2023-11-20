from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile),
    path('following/<int:user_pk>/', views.following),
    path('follower/<int:user_pk>/', views.follower),
]
