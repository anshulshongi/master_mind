"""master_mind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views
from blog.models import blog

# 
urlpatterns = [
    
    path('',views.index),
    path('article/',views.article),
    path('neet/',views.neet),
    
]

# 
extended_patterns = [

]

raw_qs = blog.objects.all()

# for i in raw_qs:
#     urlpatterns.append(path(str(i.)))