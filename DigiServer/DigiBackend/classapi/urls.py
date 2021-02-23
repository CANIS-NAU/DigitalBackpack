from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('googlelogin/', views.GoogleSignup, name='GoogleSignUp'),  
    path('courses/', views.courses, name='Courses'), 
    path('courseworks/', views.courseworks, name='Coursework'), 
    path('submissions/', views.submissions, name='Submissions'), 
    path('announcements/', views.announcements, name='Announcements'), 
    path('upload/', views.upload, name='AssignementUpload'), 
    path('grades/', views.grades, name='Grades'), 
]