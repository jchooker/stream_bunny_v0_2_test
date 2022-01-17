from django.urls import path
from . import views

urlpatterns = [
    path('',views.favorite_movies_main_page),
    path('movie_info_discussion_page',views.movie_info_discussion_page),
    path('user_favorite_movies_page',views.user_favorite_movies_page),
    path('user_info_page_edit',views.user_info_page_edit),
    path('user_info_page',views.user_info_page), 
    path('discussion_partial',views.discussion_partial),
    path('discussion_partial_edit',views.discussion_partial_edit),
]