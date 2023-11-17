from django.db.models import Avg, Count
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie, Review


def update_average_rating(instance):
    reviews = Review.objects.filter(movie=instance.movie)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    cnt_rating = reviews.aggregate(Count('rating'))['rating__count'] or 0
    
    instance.movie.rating_avg = avg_rating
    instance.movie.rating_cnt = cnt_rating
    instance.movie.save()


@receiver(post_save, sender=Review)
def update_movie_average_rating_after_save(sender, instance, **kwargs):
    update_average_rating(instance)


@receiver(post_delete, sender=Review)
def update_movie_average_rating_after_delete(sender, instance, **kwargs):
    update_average_rating(instance)


