from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=1000)
    student_id = models.CharField(max_length=1000)
    student_roll = models.CharField(max_length=1000, primary_key=True)
    password = models.CharField(max_length=1000)


class Cse(models.Model):
    dsa = models.CharField(max_length=1000)
    oops = models.CharField(max_length=1000)
    dbms = models.CharField(max_length=1000)
    Computer_Networks = models.CharField(max_length=1000)
    os = models.CharField(max_length=1000)
    communication = models.CharField(max_length=1000)
    jee_mains = models.CharField(max_length=1000)
    cp = models.CharField(max_length=1000)
    student_id = models.CharField(max_length=1000, primary_key=True)