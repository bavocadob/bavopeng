from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Profile
from .models import Article, Comment


User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('nickname',)
    
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'profile',)



class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id',)

    article = ArticleSerializer(read_only=True)
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'


# 단일 게시글 조회
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_cnt = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


# 전체 게시글 조회
class ArticleListSerializer(serializers.ModelSerializer):
    comment_cnt = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'created_at', 'comment_cnt',)