from wsgiref.simple_server import demoapp
from django.shortcuts import render

def index(request):
    context = {"data":"Home Page of Django App"}
    return render(request,'demoapp/index.html', context)
