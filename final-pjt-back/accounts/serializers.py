from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie
from articles.models import Article
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
        fields = ('id', 'profile',)


# 사용자 프로필 로드용 serializer
class UserPreferenceSerializer(serializers.ModelSerializer):
    class UserMoviePreferenceSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('id', 'title', 'release_date', 'backdrop_path', 'rating_avg',)

    class UserArticlePreferenceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title', 'user',)

    followers = serializers.StringRelatedField(many=True, read_only=True)
    followings_cnt = serializers.IntegerField(source='followings.count', read_only=True)
    followers_cnt = serializers.IntegerField(source='followers.count', read_only=True)
    liked_movies = UserMoviePreferenceSerializer(many=True, read_only=True)
    disliked_movies = UserMoviePreferenceSerializer(many=True, read_only=True)
    wished_movies = UserMoviePreferenceSerializer(many=True, read_only=True)
    liked_articles = UserArticlePreferenceSerializer(many=True, read_only=True)
    disliked_articles = UserArticlePreferenceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('followings_cnt', 'followings', 'followers_cnt', 'followers', 
                  'liked_movies', 'disliked_movies', 'wished_movies', 'liked_articles', 'disliked_articles')


# 프로필 조회
class ProfileSerializer(serializers.ModelSerializer):
    user = UserPreferenceSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


# 프로필 수정
class ProfileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'nickname', 'profile_img', 'introduce',)
        read_only_fields = ('user',)