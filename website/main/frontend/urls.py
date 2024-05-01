from django.urls import path
from .views import home, adminDashboard, login, userDashboard, task

urlpatterns = [
    path('login-page', login, name="login"),
    path('', home, name="home"),
    path('dash', adminDashboard, name="home"),
    path('user-dash', userDashboard, name="user-home"),
    path('task/<str:pk>', task, name="task"),
]