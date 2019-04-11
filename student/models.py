from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=1000)
    student_id = models.CharField(max_length=1000)
    student_roll = models.CharField(max_length=1000, primary_key=True)
    password = models.CharField(max_length=1000)


class Cse(models.Model):
    dsa = models.FloatField(default=50)
    oops = models.FloatField(default=50)
    dbms = models.FloatField(default=50)
    Computer_Networks = models.FloatField(default=50)
    os = models.FloatField(default=50)
    communication = models.FloatField(default=50)
    jee_mains = models.FloatField(default=50)
    cp = models.FloatField(default=50)
    compiler = models.FloatField(default=50)
    student_roll = models.CharField(max_length=1000, primary_key=True)

class CseRating(models.Model):
    dsa = models.FloatField(default=10)
    oops = models.FloatField(default=10)
    dbms = models.FloatField(default=10)
    Computer_Networks = models.FloatField(default=10)
    os = models.FloatField(default=10)
    communication = models.FloatField(default=10)
    jee_mains = models.FloatField(default=10)
    cp = models.FloatField(default=10)
    compiler = models.FloatField(default=10)
    student_roll = models.CharField(max_length=1000, primary_key=True)
    student_background = models.FloatField(default=10)
    placement_status = models.FloatField(default=0)


class StudentGen(models.Model):
    student_roll = models.CharField(max_length=1000, primary_key=True)
    percentage_in_10th = models.FloatField()
    percentage_in_12th = models.FloatField()
    current_CGPA = models.FloatField()
    year_of_birth = models.FloatField()
    expected_year_of_placement = models.FloatField()
    passing_year_of_10th = models.FloatField()
    passing_year_of_12th = models.FloatField()
    Board_10th = models.IntegerField()
    Board_12th = models.IntegerField()
    BTech_Branch = models.IntegerField()
    Category = models.IntegerField()
    Fathers_Occupation = models.IntegerField()
    Gender = models.IntegerField()
    Mothers_Occupation = models.IntegerField()
    Permanent_address = models.IntegerField()
    type_of_disability = models.IntegerField()
    placement_chance = models.FloatField(default=.5000)

