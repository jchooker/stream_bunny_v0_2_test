from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page),
    path('success',views.success),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('base',views.base),
    path('child',views.child),
]