from django.db import models

# Create your models here.e
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
