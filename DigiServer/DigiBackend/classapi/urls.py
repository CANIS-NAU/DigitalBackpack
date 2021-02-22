from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('googlelogin/', views.GoogleSignup, name='GoogleSignUp'),  
    #path('g/', views.PermissionView, name='GoogleSignUp'), 
]