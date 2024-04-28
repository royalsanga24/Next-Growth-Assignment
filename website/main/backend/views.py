from main.serializers import AppSerializer
from .models import App

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

from django.shortcuts import render
from django.shortcuts import get_list_or_404



@api_view(['GET'])
def app(request):
    apps = get_list_or_404(App)
    serializer = AppSerializer(apps, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def appCreate(request):
    serializer = AppSerializer(data=request.data, many=False)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)