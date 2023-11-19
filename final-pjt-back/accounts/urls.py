from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/profile/', views.profile),
    path('<int:user_pk>/following/', views.following),
    path('<int:user_pk>/follower/', views.follower),
]
