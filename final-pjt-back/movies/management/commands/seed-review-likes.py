from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth import get_user_model

import random
import datetime

from movies.models import Review, Movie


User = get_user_model()


class Command(BaseCommand):
    help = "리뷰 좋아요 데이터를 만듭니다."

    def handle(self, *args, **options):
        users = User.objects.all()
        movies = Movie.objects.all()

        reviews = Review.objects.all()

        for review in reviews:
            for i in range(random.randint(0, 10)):
                review.liked_by.add(random.choice(users))
        
        for movie in movies:
            if movie.review_set.count():
                for i in range(random.randint(0, 20)):
                    user = random.choice(users)
                    if not movie.liked_by.filter(pk=user.pk).exists() and not movie.disliked_by.filter(pk=user.pk).exists():
                        movie.liked_by.add(user)
                for i in range(random.randint(0, 13)):
                    user = random.choice(users)
                    if not movie.liked_by.filter(pk=user.pk).exists() and not movie.disliked_by.filter(pk=user.pk).exists():
                        movie.disliked_by.add(user)

        

