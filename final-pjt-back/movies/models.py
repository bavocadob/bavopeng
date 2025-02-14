from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
User = settings.AUTH_USER_MODEL


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    korean_name = models.TextField(blank=True)
    profile_path = models.TextField(blank=True)


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    korean_name = models.TextField(blank=True)
    profile_path = models.TextField(blank=True)


class WatchProvider(models.Model):
    name = models.TextField()
    logo_img = models.ImageField(blank=True)
    url = models.TextField()


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
    watch_providers = models.ManyToManyField(WatchProvider)
    liked_by = models.ManyToManyField(User, related_name='liked_movies')
    disliked_by = models.ManyToManyField(User, related_name='disliked_movies')
    wished_by = models.ManyToManyField(User, related_name='wished_movies')
    title = models.TextField()
    original_title = models.TextField()
    certification = models.TextField(blank=True)    # 심의등급
    overview = models.TextField(blank=True)         # 줄거리
    release_date = models.DateField()               # 개봉일
    runtime = models.IntegerField()
    tagline = models.TextField(blank=True)          # 한 줄 설명
    poster_path = models.TextField(blank=True)
    backdrop_path = models.TextField(blank=True)
    trailer = models.TextField(blank=True)
    rating_avg = models.FloatField(default=0)
    rating_cnt = models.IntegerField(default=0)


class NowShowing(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)


class Upcoming(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='liked_reviews')
    content = models.CharField(max_length=500)
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)