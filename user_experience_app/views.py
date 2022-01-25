from django.shortcuts import render,redirect,HttpResponse
from .models import *
from login_app.models import User
from stream_bunny_v0_2_app.models import Movie

def favorite_movies_main_page(request):
    user = User.objects.get(id=request.session['user_id'])

    context = {
        "name_of_page" : "favorite_movies_main_page",
        "user" : user,
        "movies" : Movie.objects.all()
    }
    return render(request,'favorite_movies_main_page.html',context)

def members_list_page(request):
    user = User.objects.get(id=request.session['user_id'])
    members = User.objects.all()
    context = {
        "name_of_page" : "members_list_page",
        "user" : user,
        "members" : members
    }
    return render(request,'members_list_page.html',context)
    
def member_profile(request, member_id):
    user = User.objects.get(id=request.session['user_id'])
    member = User.objects.get(id=member_id)
    member_likes = member.liked_by.all()
    # user_likes = user.liked_by.all()
    context ={
        "name_of_page" : "member_profile_page",
        "member" : member,
        "member_likes" : member_likes,
        "user" : user,
        # "user_liked" : user_likes,
    }
    return render(request, 'member_profile.html', context)

def movie_info_discussion_page(request):
    user = User.objects.get(id=request.session['user_id'])

    context = {
        "name_of_page" : "movie_info_discussion_page",
        "user" : user,
    }
    return render(request,'movie_info_discussion_page.html',context)
    
def user_favorite_movies_page(request):
    user = User.objects.get(id=request.session['user_id'])

    context = {
        "name_of_page" : "user_favorite_movies_page",
        "user" : user,
    }
    return render(request,'user_favorite_movies_page.html',context)
    
def user_info_page_edit(request):
    user = User.objects.get(id=request.session['user_id'])

    context = {
        "name_of_page" : "user_info_page_edit",
        "user" : user,
    }
    return render(request,'user_info_page_edit.html',context)
    
def user_info_page(request):
    user = User.objects.get(id=request.session['user_id'])
    my_likes = user.liked_by.all()

    context = {
        "name_of_page" : "user_info_page",
        "user" : user,
        "my_likes" : my_likes
    }
    return render(request,'user_info_page.html',context)
    
def comment(request):
    user = User.objects.get(id=request.session['user_id'])

    context = {
        "user" : user,
        "name_of_page" : "comment_partial (use ajax)",
    }
    return render(request,'comment_partial.html',context)
    
def response(request):
    user = User.objects.get(id=request.session['user_id'])

    context = {
        "user" : user,
        "name_of_page" : "response_partial (use ajax)",
    }
    return render(request,'response_partial.html',context)

def ue_like(request,movie_id):
    if request.method == 'POST':
        user = request.session['user']
        movie = Movie.objects.get(id=movie_id)

        # CHECK TO SEE IF THIS IS RIGHT:
        User.liked_by.delete(movie) ## ???????????

        User.liked_by
        # Note.objects.create(body=request.POST['new_note'])    
        context = {
            # 'notes' : Note.objects.all(),
        }
        return render(request,"favorite_movies_main_partial.html",context)
    return redirect('/')

def like(request, movie_id):
    user = User.objects.get(id=request.session["user_id"])

    Movie.objects.create(imdb_id = movie_id)

    movie = Movie.objects.get(id=movie_id)
    movie.liked_by.add(user)

    return render(request,"user_info_page.html")

