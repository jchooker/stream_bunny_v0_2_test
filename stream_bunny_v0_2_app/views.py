import json
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from imdb import IMDb
from django.template.defaulttags import register
from .models import *

@csrf_exempt
def movie_search(request):
    return render(request, 'movie_search.html')

def search(request, query):
    print("Change made")
    print("More changes made")
    ia = IMDb()
    curr_movies = ia.search_movie_advanced(query, adult=False)
    if curr_movies:
        movie_array = []
        for movie in curr_movies:
            if movie.get('votes'):
                movie_array.append( {
                    'title': movie.get('title'),
                    'year': movie.get('year'),
                    'rating': movie.get('rating'),
                    'genre': movie.get('genre'),
                    'poster_link': movie.get('cover url'),
                    'votes': movie.get('votes'),
                    'id': movie.getID(),
                    } )
        curr_movies = sorted(movie_array, key=lambda d: d['votes'], reverse=True)
        return HttpResponse(json.dumps(movie_array[:6]), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"no movie": "Can't find movie"}),
            content_type="application/json"
        )

def get_movie(request, movie_id):
    ia = IMDb()
    movie_detail = ia.get_movie(movie_id)
    print('*'*300)
    print(movie_detail.get("plot"))
    return redirect('/')