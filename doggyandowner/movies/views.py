import json

from django.http import JsonResponse
from django.views import View

from movies.models import *

# Create your views here.
class ActorsView(View):
    def get(self, request):
        actor_list = Actor.objects.all()
        results = []

        for i in actor_list:
            actor_movie = i.actor_movie_set.all()
            movies_list = []

            for j in actor_movie:
                movies_list.append(j.movie.title)

            results.append({
                "first name" : i.first_name,
                "last name" : i.last_name,
                "filmography" : movies_list
            })
            
        return JsonResponse({'results':results}, status=200)

class MoviesView(View):
    def get(self, request):
        movie_list = Movie.objects.all()
        results = []

        for i in movie_list:
            actor_movie = i.actor_movie_set.all()
            casting_list = []
            for j in actor_movie:
                casting_list.append(j.actor.first_name)

            results.append({
                "title" : i.title,
                "running_tile" : i.running_time,
                "cast" : casting_list
            })
            
        return JsonResponse({'results':results}, status=200)


