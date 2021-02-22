import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.db import models
from django.conf import settings


# class Classroom(models.Model):

#     service = None

#     def get_token(self):
#         """ The file token.pickle stores the user's access and refresh tokens,
#         and is created automatically when the authorization flow completes
#         for the first time"""
#         creds = None
#         if os.path.exists('token.pickle'):
#             with open('token.pickle', 'rb') as token:
#                 creds = pickle.load(token)
#                 return creds

#     def save_token(self, credentials):
#         """Save the credentials for next run"""
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(credentials, token)

#     def login(self):
#         """If there are no (valid) credentials available, let the user log in"""
#         creds = self.get_token()
#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 flow = InstalledAppFlow.from_client_secrets_file('credentials.json', settings.GOOGLE_API_SCOPES)
#                 creds = flow.run_local_server(port=0)
#                 self.save_token(credentials=creds)
#                 self.service = build('classroom', 'v1', credentials=creds)

#     def list_courses(self):
#         results = self.service.courses().list().execute()
#         return results.get('courses', [])



class Course(models.Model):
     student_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
     course_name = models.CharField('Course Name', max_length=200)
     course_grade = models.CharField('Course Grade', max_length=100)

