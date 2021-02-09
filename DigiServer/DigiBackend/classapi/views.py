import pickle
import os.path
import hashlib

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.rosters',
'https://www.googleapis.com/auth/classroom.courses.readonly',
#'https://www.googleapis.com/auth/classroom.coursework.me.readonly',
#'https://www.googleapis.com/auth/classroom.coursework.students.readonly',
'https://www.googleapis.com/auth/classroom.announcements',
]

def login(user_id):
    user_bytes = user_id.encode('utf-8')
    user = hashlib.sha256(user_bytes).hexdigest()
    creds = None
    if os.path.exists(f'static/tokens/{user}.pickle'):
        with open(f'static/tokens/{user}.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(f'static/tokens/{user}.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('classroom', 'v1', credentials=creds)

    return service

    # Call the Classroom API

def course_details(final_service):
    results = final_service.courses().list().execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
        for course in courses:
            #print(course)
            print(course['name'])
            print('Section: ',course['section'])
            print('Course State: ',course['courseState'])
            #print(course['userId'])

@api_view(['GET','POST'])
def get_studentclassinfo(request):
    pass

@api_view(['GET','POST'])
def get_subjectinfo(request):
    pass

@api_view(['GET','POST'])
def get_annoucement(request):
    pass

