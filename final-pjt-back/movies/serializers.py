from rest_framework import serializers
from .models import Genre, Movie, Director, Actor, Review

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


    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'certification', 'overview','release_date','runtime' , 'genres', 'backdrop_path', 'poster_path',
                  'actors', 'directors', 'trailer')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'liked_by',)