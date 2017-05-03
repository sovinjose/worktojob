from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class CompanyUserProfile(models.Model):
    user_profile = models.OneToOneField(User)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='cmpny_logo', blank=True, null=True)

JOB_TYPE = (
    ('Fulltime/Part-time', 'Fulltime/Part-time'),
    ('Permanent/Temporary/Contract', 'Permanent/Temporary/Contract'),
    ('Apprenticeships/Internship/Volunteer ', 'Apprenticeships/Internship/Volunteer ')
)

INDUSTRY_CHOICES = (
    ("IT-Software / Software Services", "IT-Software / Software Services"),
    ("BPO / Call Centre / ITES", "BPO / Call Centre / ITES"),
    ("Automobile / Auto Anciliary / Auto Components", "Automobile / Auto Anciliary / Auto Components"),
    ("Accounting / Finance", "Accounting / Finance"),
    ("Advertising / PR / MR / Event Management", "Advertising / PR / MR / Event Management"), 
    ("Agriculture / Dairy", "Agriculture / Dairy"),
    ("Animation / Gaming", "Animation / Gaming"),
    ("Architecture / Interior Design", "Architecture / Interior Design"),
    ("Aviation / Aerospace Firms", "Aviation / Aerospace Firms"),
    ("Banking / Financial Services / Broking", "Banking / Financial Services / Broking"),
    ("Brewery / Distillery", "Brewery / Distillery"),
    ("Broadcasting", "Broadcasting"),
    ("Consumer Electronics / Appliances / Durables", "Consumer Electronics / Appliances / Durables"),
    ("Education / Teaching / Training", "Education / Teaching / Training"),
    ("Electricals / Switchgears", "Electricals / Switchgears"),
    ("Others", "Others"),
)

MIN_SLRY = ((str(i), str(i)) for i in range(0, 31))
MAX_SLRY = ((str(i), str(i)) for i in range(0, 31))

class JobProfile(models.Model):
    company = models.ForeignKey(CompanyUserProfile)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    job_start_date = models.DateTimeField()
    salary_min = models.CharField(max_length=100, blank=True, null=True, choices=MIN_SLRY)
    salary_max = models.CharField(max_length=100, blank=True, null=True, choices=MAX_SLRY)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)


class Employe(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_start_date = models.DateTimeField()