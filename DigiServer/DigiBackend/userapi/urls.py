from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('register', views.UserViewSet, basename= 'userapi')
router.register('changepassword', views.ChangePasswordViewSet, basename= 'password')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]