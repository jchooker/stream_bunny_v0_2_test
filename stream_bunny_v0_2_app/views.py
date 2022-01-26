import json
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from imdb import IMDb
from django.template.defaulttags import register

from stream_bunny_v0_2_app.api import get_stream
from .models import *
from user_experience_app.models import *
from login_app.models import *

@csrf_exempt
def movie_search(request):
    if 'user_id' in request.session.keys():
        user = User.objects.get(id=request.session['user_id'])

        context = {
            "name_of_page" : "Stream Bunny Search Page",
            "user" : user,
            "search_page" : True,
        }
        return render(request, 'movie_search.html',context)
    context = {
        "name_of_page" : "Stream Bunny Search Page",
        "search_page" : True,
    }
    return render(request, 'movie_search.html',context)

def search(request, query):
    ia = IMDb()
    curr_movies = ia.search_movie_advanced(query, adult=False)
    print(curr_movies)
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
    # print(movie_id)
    streaming_on = get_stream(movie_id)
    if movie_detail.get('director'):
        dir_vals = movie_detail.get('director')
        dir_res = []
        for dir in dir_vals:
            dir_res = dir['name']
        movie_dict = {
            'title': movie_detail.get('title'),
            'year' : movie_detail.get('year'),
            'poster_link': movie_detail.get('cover url'),
            # 'director' : movie_detail.get('director')[0]['name'],
            'director' : dir_res,
            'plot': movie_detail.get('plot')[0],
            'streams': streaming_on,
            # 'streaming_on':[streaming_on[:]['stream']],
            # 'streaming_on':streaming_on[0]['stream'],
            # 'go_to_stream':[streaming_on[:]['stream_link']]
            # 'go_to_stream':streaming_on[0]['stream_link']
        }
    else:
        movie_dict = {
            'title': movie_detail.get('title'),
            'year' : movie_detail.get('year'),
            'poster_link': movie_detail.get('cover url'),
            'plot': movie_detail.get('plot')[0],
            'streams': streaming_on,
            # 'streaming_on':streaming_on[0]['stream'],
            # 'streaming_on':[streaming_on[:]['stream']], #expand this to include all services that carry it?
            # 'go_to_stream':[streaming_on[:]['stream_link']] #likewise - cont'd from line 77
            # 'go_to_stream':streaming_on[0]['stream_link']
        }
    return HttpResponse(json.dumps(movie_dict), content_type="application/json")


######### I can't finish the following code without help from Drew. At least the url paths are working.

def like(request, movie_id):
    if 'user_id' in request.session.keys():
        user = User.objects.get(id=request.session['user_id'])
        movie_list = Movie.objects.filter(imdb_id = movie_id)
        if len(movie_list) > 0:
            movie = movie_list[0]
            # if user not in movie.liked_by.all():
            #     pass
                # movie.liked_by = user

        else:
            ia = IMDb()
            movie = ia.get_movie(movie_id)
            this_movie = Movie.objects.create(
                imdb_id = movie_id,
                imdb_rating = movie['rating'],
                poster_link = movie['cover url'],
                # poster_low = "xxxx",
                plot = movie['plot'],
                title = movie['title'],
                year = movie['year'],
                director = movie['director'],
                genres = movie['genres'],
            )

            this_movie.liked_by.add(user)
            my_likes = user.liked_by.all()

            context ={
                "user" : user,
                "my_likes": my_likes
            }
            return render(request,"user_info_page.html", context)
            # this_movie.liked_by.set(user)

# TypeError: Direct assignment to the forward side of a many-to-many set is prohibited. Use liked_by.set() instead.
# TypeError: 'User' object is not iterable

        # return redirect("/")  #this is temporary
    else:
        return redirect("/login")



# C:\Users\jcole\OneDrive\Desktop\c dojo\python_stack\django\final_proj\stream_bunny_v0_2\stream_bunny_v0_2_app\images\hulu.png