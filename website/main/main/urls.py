from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from .views import login, signup, test_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("backend.urls")),
    re_path('login', login),
    re_path('signup', signup),
    re_path('test_token', test_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
