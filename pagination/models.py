from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.IntegerField(choices=((0, '男'), (1, '女')),null=True,blank=True)
    studentNo = models.IntegerField()
