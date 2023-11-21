from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article),
    path('article/pages/<int:page>/', views.article_list),
    path('article/<int:article_pk>/', views.article_detail),
    path('article/<int:article_pk>/comment/', views.comment),
    path('article/<int:article_pk>/comment/<int:page>/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('article/<int:article_pk>/like/', views.like_article),
    path('article/<int:article_pk>/dislike/', views.dislike_article),
    path('comment/<int:comment_pk>/like/', views.like_comment),
    path('article/image/', views.upload_image),
]
