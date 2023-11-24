from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

    # def __str__(self):s
    #     return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=250)
    sub=models.CharField(max_length=300)

    # def __str__(self):
        # return self.name


class Student(models.Model):
    name=models.CharField(max_length=255)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    Teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    image=models.CharField(max_length=400)
