from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Q

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, ArticleFormSerializer, CommentSerializer, CommentFormSerializer

import os

# Create your views here.
# 전체 게시글 조회, 게시글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article(request):
    serializer = ArticleFormSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def article_list(request, page):
    PAGE_SIZE = 20
    
    query = request.GET.get('query', None)
    querytype = request.GET.get('querytype', None)

    print(query, querytype, request.GET)

    if query is not None and querytype is not None:
        if querytype == '1':
            articles = Article.objects.filter(title__icontains=query).order_by('-created_at')
        elif querytype == '2':
            articles = Article.objects.filter(content__icontains=query).order_by('-created_at')
        elif querytype == '3':
            articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-created_at')
        else:
            articles = Article.objects.all().order_by('-created_at')
    else:
        articles = Article.objects.all().order_by('-created_at')

    
    paginator = Paginator(articles, PAGE_SIZE)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    serializer = ArticleListSerializer(articles, many=True)
    data = {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': min(page, paginator.num_pages),
        'results': serializer.data
    }
    return Response(data)


# 단일 게시글 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    article = get_object_or_404(Article.objects.select_related('user', 'ref_movie'), pk=article_pk)

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
def comment(request, article_pk):
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


# 게시글에 대한 댓글 조회
@api_view(['GET'])
def comment_list(request, article_pk, page):
    article = get_object_or_404(Article, pk=article_pk)
    PAGE_SIZE = 5
    
    comments = Comment.objects.filter(article=article).filter(parent_comment=None)

    paginator = Paginator(comments, PAGE_SIZE)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    serializer = CommentSerializer(comments, many=True)
    data = {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': min(page, paginator.num_pages),
        'results': serializer.data
    }
    return Response(data)


# 단일 댓글 수정, 삭제
@api_view(['PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated and request.user == comment.user:
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
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    if request.method == 'POST':
        if article.liked_by.filter(pk=user.pk).exists():
            article.liked_by.remove(user)
        else:
            if article.disliked_by.filter(pk=user.pk).exists():
                article.disliked_by.remove(user)
            article.liked_by.add(user)
        data = {
            'is_like' : article.liked_by.filter(pk=user.pk).exists(),
            'is_dislike' : article.disliked_by.filter(pk=user.pk).exists(),
            'like_cnt' : article.liked_by.count(),
            'dislike_cnt' : article.disliked_by.count(),
        }
        return Response(data, status=status.HTTP_200_OK)
    

# 게시글 싫어요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dislike_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    if request.method == 'POST':
        if article.disliked_by.filter(pk=user.pk).exists():
            article.disliked_by.remove(user)
        else:
            if article.liked_by.filter(pk=user.pk).exists():
                article.liked_by.remove(user)
            article.disliked_by.add(user)
        # isLike.valu
        # isDislike.v
        # likeCnt.val
        # dislikeCnt.
        data = {
            'is_like' : article.liked_by.filter(pk=user.pk).exists(),
            'is_dislike' : article.disliked_by.filter(pk=user.pk).exists(),
            'like_cnt' : article.liked_by.count(),
            'dislike_cnt' : article.disliked_by.count(),
        }
        return Response(data, status=status.HTTP_200_OK)
    

# 댓글 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user

    if request.method == 'POST':
        if comment.liked_by.filter(pk=user.pk).exists():
            comment.liked_by.remove(user)
        else:
            comment.liked_by.add(user)
        
        data = {
            'is_like' : comment.liked_by.filter(pk=user.pk).exists(),
            'like_cnt' : comment.liked_by.count(),
        }
        return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def upload_image(request):
    if request.method == 'POST':
        file = request.FILES['image']
        file_name = default_storage.save('article_images/' + file.name, ContentFile(file.read()))
        file_url = os.path.join(settings.MEDIA_URL, file_name)
        
        return Response({'url': f'http://127.0.0.1:8000{file_url}'})
    else:
        return Response({'error': 'Invalid method'})