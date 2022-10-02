
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length= 20)


class Courses(models.Model):
    name = models.CharField(max_length= 50)
    price = models.IntegerField()
    author = models.CharField(max_length=40)
    discouunt = models.IntegerField()
    duration = models.FloatField()


class Instructor(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()

    def __str__(self) :
        return self.name


class Subjects(models.Model):
    title = models.CharField(max_length= 50)
    rating = models.IntegerField()
    instructor = models.ForeignKey(Instructor , on_delete= models.CASCADE , related_name= 'subjects')
