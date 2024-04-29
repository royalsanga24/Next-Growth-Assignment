from rest_framework import serializers
from django.contrib.auth.models import User
from backend.models import App

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class AppSerializer(serializers.ModelSerializer):
    # icon = serializers.ImageField(
    #     max_length=None,
    #     use_url=True
    # )

    class Meta:
        model = App
        fields = ['name', 'link', 'category', 'sub_category']

        # def update(self, instance, validated_data):
        #     instance.icon = validated_data.get('icon', instance.icon)
        #     instance.save()
        #     return instance