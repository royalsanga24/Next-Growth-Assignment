from django.urls import path, re_path
from .views import app, appCreate

urlpatterns = [
    re_path('apps', app),
    re_path('create-app', appCreate),
]
