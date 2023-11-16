from django.db import models

# Create your models here.
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


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
    title = models.TextField()
    original_title = models.TextField()
    certification = models.TextField(blank=True)    # 심의등급
    overview = models.TextField(blank=True)         # 줄거리
    release_date = models.DateField()               # 개봉일
    runtime = models.IntegerField()
    tagline = models.TextField(blank=True)          # 한 줄 설명
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    trailer = models.TextField()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    