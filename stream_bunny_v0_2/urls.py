# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('stream_bunny_v0_2_app.urls')),
    path('login/', include('login_app.urls')),
    path('user_experience/', include('user_experience_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)