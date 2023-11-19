from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
User = settings.AUTH_USER_MODEL


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_movie = models.ForeignKey(Movie, blank=True, null=True, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='liked_articles')
    disliked_by = models.ManyToManyField(User, related_name='disliked_articles')
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='article/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 부모댓글만 필터링
    def get_parent_comments(self):
        return self.comments.filter(parent_comment=None)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank= True, on_delete=models.CASCADE, related_name='replies')
    liked_by = models.ManyToManyField(User, related_name='liked_comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)