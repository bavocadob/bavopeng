from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie, Review
from articles.models import Article, Comment
from .models import Profile


class CustomRegisterSerializer(RegisterSerializer):
    # nickname = serializers.CharField(
    #     required=False,
    #     allow_blank=True,
    #     max_length=255
    # )

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            # 'nickname': self.validated_data.get('nickname', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


User = get_user_model()


# ForeignKey user serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('nickname', 'profile_img',)
    
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile',)


# 사용자 프로필 로드용 serializer
class UserDetailSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('id', 'title', 'poster_path', 'rating_avg',)

    class ArticleSerializer(serializers.ModelSerializer):
        liked_cnt = serializers.IntegerField(source='liked_by.count', read_only=True)

        class Meta:
            model = Article
            fields = ('id', 'title', 'created_at', 'liked_cnt')
    
    class ReviewSerializer(serializers.ModelSerializer):
        liked_cnt = serializers.IntegerField(source='liked_by.count', read_only=True)

        class Meta:
            model = Review
            fields = ('id', 'content', 'rating', 'created_at', 'liked_cnt')
    
    class CommentSerializer(serializers.ModelSerializer):
        liked_cnt = serializers.IntegerField(source='liked_by.count', read_only=True)

        class Meta:
            model = Comment
            fields = ('id', 'content', 'created_at', 'liked_cnt')


    followings_cnt = serializers.IntegerField(source='followings.count', read_only=True)
    followers_cnt = serializers.IntegerField(source='followers.count', read_only=True)
    liked_movies = MovieSerializer(many=True, read_only=True)
    wished_movies = MovieSerializer(many=True, read_only=True)
    liked_articles = ArticleSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only = True)
    article_set = ArticleSerializer(many=True, read_only = True)
    comment_set = CommentSerializer(many=True, read_only = True)

    class Meta:
        model = User
        fields = ('id', 'followings_cnt', 'followers_cnt', 
                  'liked_movies', 'wished_movies', 'liked_articles', 'wished_movies', 'review_set', 'article_set', 'comment_set')


# 프로필 조회
class ProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('nickname', 'user', 'profile_img', 'introduce',)


# 프로필 수정
class ProfileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'nickname', 'profile_img', 'introduce',)
        read_only_fields = ('user',)
        

# 팔로잉, 팔로우 조회
class UserFollowSerializer(serializers.ModelSerializer):
    class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('nickname', 'profile_img')
    
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')
