from rest_framework import serializers
from .models import student_info


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_info
        fields = ['student_name', 'student_email', 'student_roll']