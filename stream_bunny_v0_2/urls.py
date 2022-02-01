# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('stream_bunny_v0_2_app.urls')),
    path('login/', include('login_app.urls')),
    path('user_experience/', include('user_experience_app.urls')),
]
