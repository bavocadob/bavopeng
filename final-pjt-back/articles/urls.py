from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:article_pk>/', views.article_detail),
    path('article/<int:article_pk>/comment/', views.comment_create),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('article/<int:article_pk>/like/', views.like_article),
    path('article/<int:article_pk>/dislike/', views.dislike_article),
    path('comment/<int:comment_pk>/like/', views.like_comment),
]
