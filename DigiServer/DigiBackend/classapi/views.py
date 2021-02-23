from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from userapi.models import User
from userapi.serializers import UserSerializer
from userapi.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .gLoginAuth import GoogleLogin
from rest_framework.decorators import api_view


@api_view(['GET'])
def GoogleSignup(request):
    user_id = request.user.email
    user_person = GoogleLogin()
    creds = user_person.login(user_id)
    user = {
        'username':user_id
    }
    return Response(user)

@api_view(['GET'])
def getCourse(request):
    user_id = request.user.email
    user_person = GoogleLogin()
    creds = user_person.login(user_id)
    service = build('classroom', 'v1', credentials=creds)
    results = service.courses().list().execute()
    courses = results.get('courses', [])

    if not courses:
        content={
            'message':'No courses found.',
        }
        return Response(content)
    else:
        for course in courses:
            #print(course)
            print(course['name'])
            print('ID: ',course['id'])
            print('Section: ',course['section'])
            print('Course State: ',course['courseState'])
            #print(course['userId'])
    pass

@api_view(['GET'])
def courses(request):
    pass

@api_view(['GET'])
def courseworks(request):
    pass

@api_view(['GET'])
def submissions(request):
    pass

@api_view(['GET'])
def announcements(request):
    pass

@api_view(['GET'])
def grades(request):
    pass

@api_view(['GET','POST'])
def upload(request):
    pass