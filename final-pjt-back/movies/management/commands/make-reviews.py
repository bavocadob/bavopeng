from django.core.management.base import BaseCommand
import requests
import json

from movies.models import Movie
from django.conf import settings
import random

API_KEY = settings.API_KEY


class Command(BaseCommand):
    def handle(self, *args, **options):
        movies = Movie.objects.all()
        
        json_results = []
        for movie in movies:
            try:
                url = f"https://api.themoviedb.org/3/movie/{movie.id}/reviews?language=en-US&page=1"
                params = {
                    'api_key': API_KEY,
                    'language': 'en-US',
                    'page' : 1
                }
                
                response = requests.get(url, params=params).json()
                if response.get('total_results') < 3:
                    continue

                for i in range(1, response.get('total_pages') + 1):
                    params = {
                        'api_key': API_KEY,
                        'language': 'en-US',
                        'page' : i
                    }

                    response = requests.get(url, params=params).json()
                    results = response.get('results')
                    for review in results:
                        rating = review.get('author_details').get('rating')
                        if rating is not None:
                            data = {
                                'rating' : int(rating),
                                'movieId' : movie.id,
                                'userId' : random.randint(1, 1000)
                            }
                            json_results.append(data)
            except:
                continue

        # Write json_results to a new file
        with open('movies/fixtures/reviews_new.json', 'w', encoding='utf-8') as f:
            json.dump(json_results, f, ensure_ascii=False, indent=4)
