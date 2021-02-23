from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('customsearch/<str:query>/', views.custom_query, name='CustomSearch'), 
    path('googlesearch/<str:query>/', views.google_query, name='CustomSearch'),  
]