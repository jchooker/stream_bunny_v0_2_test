from django.urls import path
from . import views

urlpatterns = [
    path('',views.favorite_movies_main_page),
    path('movie_info_discussion_page',views.movie_info_discussion_page),
    path('user_favorite_movies_page',views.user_favorite_movies_page),
    path('user_info_page_edit',views.user_info_page_edit),
    path('user_info_page',views.user_info_page), 
    path('members_list_page',views.members_list_page), 
    path('comment',views.comment),
    path('response',views.response), 
    path('like/<int:movie_id>',views.ue_like), 
]