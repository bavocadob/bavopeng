import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
import django
django.setup()

from movies.models import Movie, Actor, Director, Genre, WatchProvider


import csv

def backup_model(model, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [f.name for f in model._meta.fields]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for obj in model.objects.all():
            writer.writerow({field: getattr(obj, field) for field in fieldnames})


def backup_m2m(model, m2m_field_name, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # 헤더 작성
        writer.writerow([model.__name__.lower(), m2m_field_name])

        # 각 객체에 대해 ManyToManyField를 쿼리
        for obj in model.objects.all():
            related_objs = getattr(obj, m2m_field_name).all()
            for related_obj in related_objs:
                writer.writerow([obj.pk, related_obj.pk])


backup_model(Movie, 'movies.csv')
backup_model(Actor, 'actors.csv')
backup_model(Director, 'directors.csv')
backup_model(Genre, 'genres.csv')
backup_model(WatchProvider, 'watchproviders.csv')

backup_m2m(Movie, 'actors', 'movie_actors.csv')
backup_m2m(Movie, 'directors', 'movie_directors.csv')
backup_m2m(Movie, 'genres', 'movie_genres.csv')
backup_m2m(Movie, 'watch_providers', 'movie_watchproviders.csv')
