from django.urls import path, re_path
from .views import app, appCreate, appDetail, taskComplete


urlpatterns = [
    re_path('apps', app),
    re_path('create-app', appCreate),
    path('app-detail/<str:pk>', appDetail, name="app-detail"),
    path('task-complete/', taskComplete, name="task-complete")
]
