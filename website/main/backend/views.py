from main.serializers import AppSerializer
from .models import App

from io import BytesIO
import urllib
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from django.shortcuts import get_list_or_404

from PIL import Image as PILImage



@api_view(['GET'])
def app(request):
    apps = get_list_or_404(App)
    serializer = AppSerializer(apps, many=True)
    print(serializer.data[0]['name'])
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def appCreate(request):
    serializer = AppSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Invalid")
    obj = App.objects.get(name=serializer.data['name'])
    obj.icon = request.FILES.get('icon')
    obj.save()
    print(obj)
    # serializer.data[0]['icon'] = obj.icon
    print(dir(serializer.data))
    return Response(serializer.data)

