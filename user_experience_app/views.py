from django.shortcuts import render,redirect,HttpResponse
from .models import *

def favorite_movies_main_page(request):
    context = {
        "name_of_page" : "favorite_movies_main_page",
    }
    return render(request,'favorite_movies_main_page.html',context)
    
def movie_info_discussion_page(request):
    context = {
        "name_of_page" : "movie_info_discussion_page",
    }
    return render(request,'movie_info_discussion_page.html',context)
    
def user_favorite_movies_page(request):
    context = {
        "name_of_page" : "user_favorite_movies_page",
    }
    return render(request,'user_favorite_movies_page.html',context)
    
def user_info_page_edit(request):
    context = {
        "name_of_page" : "user_info_page_edit",
    }
    return render(request,'user_info_page_edit.html',context)
    
def user_info_page(request):
    context = {
        "name_of_page" : "user_info_page",
    }
    return render(request,'user_info_page.html',context)
    
def comment(request):
    context = {
        "name_of_page" : "comment_partial (use ajax)",
    }
    return render(request,'comment_partial.html',context)
    
def response(request):
    context = {
        "name_of_page" : "response_partial (use ajax)",
    }
    return render(request,'response_partial.html',context)
