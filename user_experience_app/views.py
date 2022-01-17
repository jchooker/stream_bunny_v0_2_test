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
    
def discussion_partial(request):
    context = {
        "name_of_page" : "discussion_partial",
    }
    return render(request,'discussion_partial.html',context)
    
def discussion_partial_edit(request):
    context = {
        "name_of_page" : "discussion_partial_edit",
    }
    return render(request,'discussion_partial_edit.html',context)
