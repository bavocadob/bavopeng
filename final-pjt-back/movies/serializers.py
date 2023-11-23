from rest_framework import serializers
from .models import Genre, Movie, Director, Actor, Review
from django.contrib.auth import get_user_model
from accounts.serializers import UserProfileSerializer
from articles.models import Article
from bs4 import BeautifulSoup

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'release_date','runtime', 'poster_path', 'rating_avg', 'rating_cnt')


class MovieSerializer(serializers.ModelSerializer):
    class DirectorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = '__all__'

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'

    class ReviewSerializer(serializers.ModelSerializer):
        user = UserProfileSerializer(read_only=True)
        class Meta:
            model = Review
            fields = '__all__'

    class ArticleSerializer(serializers.ModelSerializer):
        first_img = serializers.SerializerMethodField()
        content = serializers.SerializerMethodField()
        class Meta:
            model = Article
            fields = ('id', 'title', 'content', 'first_img')
        
        def get_first_img(self, obj):
            soup = BeautifulSoup(obj.content, 'html.parser')
            img_tag = soup.find('img')
            return img_tag['src'] if img_tag else None
        
        def get_content(self, obj):
            soup = BeautifulSoup(obj.content, 'html.parser')
            text = soup.get_text()
            return text

    is_like = serializers.SerializerMethodField()
    is_dislike = serializers.SerializerMethodField()
    is_wish = serializers.SerializerMethodField()
    like_cnt = serializers.IntegerField(source='liked_by.count', read_only=True)
    dislike_cnt = serializers.IntegerField(source='disliked_by.count', read_only=True)

    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    article_set = ArticleSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'certification', 'overview','release_date','runtime' , 'genres', 'backdrop_path', 'poster_path',
                  'actors', 'directors', 'trailer', 'rating_avg', 'rating_cnt', 'review_set', 'article_set' ,'is_like', 'is_dislike', 'is_wish', 'like_cnt', 'dislike_cnt')


    def get_is_like(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.liked_by.filter(id=user.id).exists()
        return False

    def get_is_dislike(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.disliked_by.filter(id=user.id).exists()
        return False

    def get_is_wish(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.wished_by.filter(id=user.id).exists()
        return False


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'liked_by',)


class MovieSimpleSerializer(serializers.ModelSerializer):
    is_like = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'is_like',)

    def get_is_like(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.liked_by.filter(id=user.id).exists()
        return False