from django.contrib import admin
from .models import student_info

# Register your models here.
@admin.register(student_info)
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_roll','student_name']
