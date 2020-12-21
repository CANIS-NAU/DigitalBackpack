from django.db import models

# Create your models here.

class student_info(models.Model):
    student_name = models.CharField(max_length=70)
    student_email = models.EmailField(max_length=100)
    student_roll = models.IntegerField()
