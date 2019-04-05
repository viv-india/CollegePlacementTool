from django.db import models


class Job(models.Model):
    skills_required = models.CharField(max_length=1000)
    ctc = models.CharField(max_length=1000)
    date_of_visit = models.CharField(max_length=1000)
    openings = models.CharField(max_length=1000)
    rounds = models.CharField(max_length=1000)
    company_id = models.CharField(max_length=1000)
    job_id = models.CharField(max_length=1000, primary_key=True)


class Company(models.Model):
    company_name = models.CharField(max_length=1000)
    company_id = models.CharField(max_length=1000,primary_key=True)
    password = models.CharField(max_length=1000)
