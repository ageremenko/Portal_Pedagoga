from pathlib import Path
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from demoapp import views

urlpatterns = [
    path("", views.index,name="index"),
    path('export/', views.export_data, name='export'),
]

