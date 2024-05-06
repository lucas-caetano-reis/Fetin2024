"""
URL configuration for Alexandria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.http import HttpResponse -----> tirar o # se necessário HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

urlpatterns = [
    path('admin/', admin.site.urls, name="Administração"), #leva ao site da administração
    path('', login, name="Login"), #quando o usuário abrir o site, ele será levado à tela de login
    path('cadastro/', cadastro, name="Cadastro") #leva o usuário à tela de cadastro
]
