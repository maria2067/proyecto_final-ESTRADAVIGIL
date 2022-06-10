from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', views.account_register,name="register"),
    path('profile/', views.account_profile,name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name= "accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
]



# accounts/login
# accounts/register
# accounts/profile