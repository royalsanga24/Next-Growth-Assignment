from django.shortcuts import render, redirect
from .forms import AppForm, CompleteTaskForm
import requests
import json

def home(request):
    return render(request, 'base.html')

def login(request):
    url = "http://127.0.0.1:8000/login"
    body = {"username": "test1", "password": "test1"}
    response = requests.post(url, data=body)
    print(response.json())
    return redirect('home')

def adminDashboard(request):
    url_create_app = "http://127.0.0.1:8000/api/create-app"
    headers = {
        "Authorization": "Token 1799e175e2ff4e2bf77d19bebdaf6eb875c00869"
    }
    form = AppForm()
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print(type(data))
            # data = json.dumps(data)
            # data = json.loads(data)
            response = requests.post(url_create_app, data=data, headers=headers)
            print(response.json())

    return render(request, 'admin-dashboard.html', {'form': form})

def userDashboard(request):
    url_get_apps = "http://127.0.0.1:8000/api/apps"
    headers = {
        "Authorization": "Token 1799e175e2ff4e2bf77d19bebdaf6eb875c00869"
    }
    response = requests.get(url_get_apps, headers=headers)
    # print(response.json())
    return render(request, 'user-dashboard.html', {"data": response.json()})

def task(request, pk):
    url_get_apps = "http://127.0.0.1:8000/api/task-complete/"
    print(url_get_apps)
    headers = {
        "Authorization": "Token 1799e175e2ff4e2bf77d19bebdaf6eb875c00869"
    }
    response = requests.get(url_get_apps, headers=headers)
    form = CompleteTaskForm()
    if request.method == "POST":
        form = CompleteTaskForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            
    return render(request, 'task.html', {"data": response.json(), "form": form})