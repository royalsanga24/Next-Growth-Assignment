from rest_framework import serializers
from django.contrib.auth.models import User
from backend.models import App, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class AppCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['name', 'link', 'category', 'sub_category']

class TaskCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"