from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField
    address = models.CharField(max_length=20)
    faculty_choices = (
        ('BCA','bca')
        ('BBA','bba')
        ('MCA','mca')

    )
    faculty = models.CharField(max_length=10)