from rest_framework import serializers
from .models import Course
from rest_framework.response import Response




class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('roll','phone', 'address', 'subject')