from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.user.is_authenticated:
        if request.user == article.user:
            if request.method == 'PUT':
                serializer = ArticleSerializer(article, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
            
            elif request.method == 'DELETE':
                article.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            data = {
                'message': '권한이 없습니다.'
            }
            return Response(data, status=status.HTTP_403_FORBIDDEN)
    else:
        data = {
            'message': '유효한 인증자격이 없습니다.'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)