from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    address = models.CharField(max_length=20)
    faculty_choices = (
        ('BCA','bca'),
        ('BBA','bba'),
        ('MCA','mca')

    )
    faculty = models.CharField(max_length=10, choices=faculty_choices)
    def __str__(self):
        return self.name