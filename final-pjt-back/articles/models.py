from django.db import models
from movies.models import Movie
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ref_movie = models.ForeignKey(Movie, blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='article/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)