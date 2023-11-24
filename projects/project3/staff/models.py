from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

class Batch(models.Model):
    name=models.CharField(max_length=200)
    


class Teacher(models.Model):
    name=models.CharField(max_length=200)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
 

class Student(models.Model):
    name=models.CharField(max_length=200)
    Batc=models.ForeignKey(Batch,on_delete=models.CASCADE)
    teach=models.ForeignKey(Teacher,on_delete=models.CASCADE)