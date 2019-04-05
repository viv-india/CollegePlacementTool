from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=1000)
    student_id = models.CharField(max_length=1000)
    student_roll = models.CharField(max_length=1000, primary_key=True)
    password = models.CharField(max_length=1000)
