from django.shortcuts import render,redirect,HttpResponse
from .models import *
from login_app.models import User
# from stream_bunny_v0_2_app.models import Movie
from stream_bunny_v0_2_app.models import Movie, Discussion, Comment
# from user_experience_app.models import Discussion, Comment

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
        "movies" : member.liked_by.all(),
        # "user_liked" : user_likes,
    }
    return render(request, 'member_profile.html', context)

def movie_info_discussion_page(request,movie_id):
    user = User.objects.get(id=request.session['user_id'])
    movie = Movie.objects.get(id=movie_id)

    context = {
        "name_of_page" : "movie_info_discussion_page",
        "user" : user,
        "movie" : movie,
    }
    return render(request,'movie_info_discussion_page.html',context)

    
def user_favorite_movies_page(request,member_id):
    member = User.objects.get(id=member_id)

    context = {
        "name_of_page" : "user_favorite_movies_page",
        "member" : member,
        "movies" : member.liked_by.all(),
        "user" : User.objects.get(id=request.session['user_id']),

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
    # my_likes = user.liked_by.all()

    context = {
        "name_of_page" : "user_info_page",
        "user" : user,
        "movies" : user.liked_by.all(),
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

def ue_like(request,movie_id,origin_page):
    if request.session['user_id']:
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        movie = Movie.objects.get(id=movie_id)
        if movie in user.liked_by.all():
            user.liked_by.remove(movie) 
        else:
            user.liked_by.add(movie)
        return HttpResponse(movie.liked_by.all().count())
    return redirect('/')

def like(request, movie_id):
    user = User.objects.get(id=request.session["user_id"])

    Movie.objects.create(imdb_id = movie_id)

    movie = Movie.objects.get(id=movie_id)
    movie.liked_by.add(user)

    return render(request,"user_info_page.html")



# MATTHEW'S DISCUSSION WORK (for "movie_discussion.html")
def movie_discussion_page(request,movie_id):
    user = User.objects.get(id=request.session['user_id'])
    movie = Movie.objects.get(id=movie_id)
    # discussion = Discussion.objects.filter(id=movie_id)
    discussions = Discussion.objects.all()
    context = {
        "name_of_page" : "movie_info_discussion_page",
        "user" : user,
        "movie" : movie,
        "discussions" : discussions,
    }
    return render(request,'movie_discussion.html',context)

def discuss(request, movie_id):
    print(movie_id)
    Discussion.objects.create(
        user = User.objects.get(id=request.session['user_id']),
        movie = Movie.objects.get(id=movie_id),
        content = request.POST['discuss']
    )

    # discussions = Discussion.objects.filter(id=movie_id)
    discussions = Discussion.objects.all()
    context ={
        "discussions" : discussions
    }
    return redirect(f'/user_experience/movie_discussion/{movie_id}', context)

# def comment(request,  movie_id, discussion_id):
def comment(request, discussion_id):
    Comment.objects.create(
        user = User.objects.get(id=request.session['user_id']),
        discussion = Discussion.objects.get(id=discussion_id),
        comment = request.POST['comment']
    )
    return render(request,'user_favorite_movies_page.html')
    # return render(request,'movie_discussion.html')

def delete_discussions(request):
    Discussion.objects.all().delete()
    return render(request,'user_favorite_movies_page.html')
