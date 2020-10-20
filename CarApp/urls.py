from django.contrib import admin
from django.urls import path,include
from CarApp import views


urlpatterns = [
    path('', views.index),
]