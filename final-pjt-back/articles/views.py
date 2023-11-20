from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, ArticleFormSerializer, CommentSerializer, CommentFormSerializer

# Create your views here.
# 전체 게시글 조회, 게시글 생성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.user.is_authenticated and request.method == 'POST':
        serializer = ArticleFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        data = {'detail': 'Authentication credentials were not provided.'}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
        

# 단일 게시글 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    article = get_object_or_404(Article.objects.select_related('user', 'ref_movie').prefetch_related('comments__replies'), pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.user.is_authenticated and request.user == article.user:
        if request.method == 'PUT':
            serializer = ArticleFormSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        
        elif request.method == 'DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        data = {'detail': 'Authentication credentials were not provided.'}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
    

# 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        parent_comment_id = request.data.get('parent_comment_id')

        if parent_comment_id: 
            parent_comment = get_object_or_404(Comment, id=parent_comment_id)
        else:
            parent_comment = None

        serializer = CommentFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article, parent_comment=parent_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 댓글 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.user.is_authenticated and request.user == comment.user:
        if request.method == 'PUT':
            serializer = CommentFormSerializer(comment, request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        
        elif request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    else:
        data = {'detail': 'Authentication credentials were not provided.'}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
    

# 게시글 좋아요
@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST' and not article.liked_by.filter(pk=request.user.pk).exists():
        if article.disliked_by.filter(pk=request.user.pk).exists():
            article.disliked_by.remove(request.user)
        article.liked_by.add(request.user)
        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE' and article.liked_by.filter(pk=request.user.pk).exists():
        article.liked_by.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

# 게시글 싫어요
@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def dislike_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST' and not article.disliked_by.filter(pk=request.user.pk).exists():
        if article.liked_by.filter(pk=request.user.pk).exists():
            article.liked_by.remove(request.user)
        article.disliked_by.add(request.user)
        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE' and article.disliked_by.filter(pk=request.user.pk).exists():
        article.disliked_by.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)