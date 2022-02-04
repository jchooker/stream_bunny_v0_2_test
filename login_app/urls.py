from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page),
    path('success',views.success),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('child',views.child),
    path('about_me', views.about_me_page),
    path('about_me_save', views.about_me_save),
]

