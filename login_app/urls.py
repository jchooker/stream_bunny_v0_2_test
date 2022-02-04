from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page),
    path('success',views.success),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('child',views.child),
    path('about_me/<int:user_id>', views.about_me),
]