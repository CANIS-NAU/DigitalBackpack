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
    log = user_person.login(user_id)
    user = {
        'username':user_id
    }
    return Response(user)