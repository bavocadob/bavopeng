from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from movies.models import Movie, Review
from articles.models import Article, Comment

# Create your models here.
class User(AbstractUser):
    

    username = models.CharField(max_length=30, unique=True)
    # nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        # nickname = data.get('nickname')

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, 'first_name', first_name)
        if last_name:
            user_field(user, 'last_name', last_name)
        # if nickname:
        #     user_field(user, 'nickname', nickname)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        
        self.populate_username(request, user)
        if commit:
            user.save()
        return user 


class Profile(models.Model):
    def user_directory_path(instance, filename):
        return f'user_{instance.user.id}'
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    likes_movies = models.ManyToManyField(Movie, related_name='liked_users')
    dislikes_movies = models.ManyToManyField(Movie, related_name='disliked_users')
    wishes_movies = models.ManyToManyField(Movie, related_name='wished_users')
    likes_reviews = models.ManyToManyField(Review, related_name='liked_users')
    likes_articles = models.ManyToManyField(Article, related_name='liked_users')
    dislikes_articles = models.ManyToManyField(Article, related_name='disliked_users')
    likes_comments = models.ManyToManyField(Comment, related_name='liked_users')
    profile_img = models.ImageField(blank=True, upload_to=user_directory_path)
    introduce = models.CharField(max_length=250, blank=True)
    nickname = models.CharField(max_length=255, unique=True)