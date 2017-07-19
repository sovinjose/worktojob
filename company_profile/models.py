from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

profile_pic = FileSystemStorage(
    location='static/profile_pic/'
)


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	logo = models.ImageField(storage=profile_pic, upload_to='%Y-%m-%d', blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	mob_number = models.CharField(max_length=100, blank=True, null=True)


class CompanyUserProfile(models.Model):
    user_profile = models.OneToOneField(User)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(max_length=100, blank=True, null=True)
    short_introduction  = models.TextField(blank=True, null=True)
    founded_in = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    vision = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)

    contact_details = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    logo = models.ImageField(storage=profile_pic, upload_to='cmpny_logo', blank=True, null=True)
    banner = models.ImageField(storage=profile_pic, upload_to='cmpny_banner', blank=True, null=True)


JOB_TYPE = (
    ('Permanent', 'Permanent'),
    ('Temporary', 'Temporary'),
    ('Freelance', 'Freelance'),
    ('Remote', 'Remote'),
    ('Internship', 'Internship'),
    ('Apprenticeship', 'Apprenticeship'),
    ('Volunteer', 'Volunteer'),
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'),
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
SALARY_TYPE_CHOICES = (
        ('Per Annum', 'Per Annum'),
        ('Per Hour', 'Per Hour')
    )


JOB_PERIOD = (
    ('Years', 'Years'),
    ('Months', 'Months'),
    ('Weeks', 'Weeks'),
)

MIN_DEGREE_QUALIFICATION = (
    ('PhD', 'PhD'),
    ('Masters', 'Masters'),
    ('Bachelors', 'Bachelors'),
    ('Diploma', 'Diploma')
)

SPONSOR_VISA = (
    ('YES', 'YES'),
    ('NO', 'NO'),
)

WORK_EXPERINCE_YEAR = ((str(i), str(i)) for i in range(0, 20))
WORK_EXPERINCE_MONTH = ((str(i), str(i)) for i in range(0, 13))
IND_EXPERINCE_YEAR = ((str(i), str(i)) for i in range(0, 20))
IND_EXPERINCE_MONTH = ((str(i), str(i)) for i in range(0, 13))

class JobProfile(models.Model):
    company = models.ForeignKey(CompanyUserProfile)
    job_description = models.TextField()
    job_start_date = models.DateField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100, null=True, blank=True)
    subject_category = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE, )
    sponsor_visa = models.CharField(max_length=100, choices=SPONSOR_VISA, null=True, blank=True)
    salary_type = models.CharField(max_length=100, choices=SALARY_TYPE_CHOICES)
    certifications = models.CharField(max_length=100, blank=True, null=True)
    job_period_data =  models.CharField(max_length=100, blank=True, null=True)
    salary_min = models.CharField(max_length=100, choices=MIN_SLRY)
    salary_max = models.CharField(max_length=100, choices=MAX_SLRY)
    job_period = models.CharField(max_length=100, blank=True, null=True, choices=JOB_PERIOD)
    industry_exp_year = models.CharField(max_length=100, choices=IND_EXPERINCE_YEAR, null=True, blank=True)
    work_experience_year = models.CharField(max_length=100, choices=WORK_EXPERINCE_YEAR)
    min_degree_qulification = models.CharField(max_length=100, blank=True, null=True, choices=MIN_DEGREE_QUALIFICATION)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_subject_cateogry_name(self):
        return self.subject_sub_category


class TechSkill(models.Model):
    text = models.CharField(max_length=100)
    job_profile = models.ForeignKey(JobProfile)


EMP_STATUS = (
    ('available', 'available'),
    ('send invitation', 'send invitation'),
    ('invitation accepted', 'invitation accepted'),
)

class Employe(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=EMP_STATUS, default="online")
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_start_date = models.DateTimeField()

