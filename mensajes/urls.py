from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import include
from . import views



urlpatterns = [
    path('', views.pagina_principal_mensajes),
]