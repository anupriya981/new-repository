from django.contrib import admin
from .models import *
# Register your models here.


class Department_display(admin.ModelAdmin):
    list_display=['name']
# admin.site.register(Department,Department_display)

class Teacher_display(admin.ModelAdmin):
    list_display=['name','sub']


class Student_display(admin.ModelAdmin):
    list_display=['name','dept','Teacher']


admin.site.register(Department,Department_display)
admin.site.register(Teacher,Teacher_display)

admin.site.register(Student,Student_display)