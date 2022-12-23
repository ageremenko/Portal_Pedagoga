"""demodjango URL Configuration

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
     https://docs.djangoproject.com/en/3.1/topics/http/urls/
Примеры:
Представления функций
     1. Добавляем import: from demoapp import views
     2. Добавляем URL-адрес в urlpatterns: path('', views.home, name='home')
Представления на основе классов
     1. Добавляем импорт: from other_app.views import Home
     2. Добавляем URL-адрес в шаблоны URL-адресов: path('', Home.as_view(), name='home')
Включение другой конфигурации URL
     1. Импортируем функцию include(): from django.urls import include, path
     2. Добавляем URL-адрес в urlpatterns: path('admin/', include('admin.site.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#for debugtool baar
#from django.conf import settings
#from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('demoapp.urls')),
]
