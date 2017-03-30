from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


COMPANY_TYPE_CHOICE = (

        ('Consultant', 'Consultant'),
        ('Company', 'Company')
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

COMPANY_SIZE = (
        ('1 - 5 employees', '1 - 5 employees'),
        ('6 - 16 employees', '6 - 16 employees'),
        ('17 - 99 employees', '17 - 99 employees'),
        ('100 - 420 employees', '100 - 420 employees'),
        ('421 - 1000 employees', '421 - 1000 employees'),
        ('1001 - 5000 employees', '1001 - 5000 employees'),
        ('5000+ employees', '5000+ employees'),

    )


class CompanyProfile(models.Model):
    user_profile = models.OneToOneField(User)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    company_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True, choices=INDUSTRY_CHOICES)
    company_size = models.CharField(max_length=100, blank=True, null=True, choices=COMPANY_SIZE)
    address = models.TextField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkdin_page = models.URLField(blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='cmpny_logo', blank=True, null=True)




FUNCTIONAL_AREA_CHOICES = (
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
)

QUALIFICATIONS = (
                ('Graduation', 'Graduation'),
                ('Post Graduation', 'Post Graduation'),
                ('Ph.D', 'Ph.D'),
)

MIN_EXPERINCE = ((str(i), str(i)) for i in range(0, 31))
MAX_EXPERINCE = ((str(i), str(i)) for i in range(0, 31))

NO_OPENINGS = ((str(i), str(i)) for i in range(0, 20))


JOB_TYPE = (
    ('Fulltime/Part-time', 'Fulltime/Part-time'),
    ('Permanent/Temporary/Contract', 'Permanent/Temporary/Contract'),
    ('Apprenticeships/Internship/Volunteer ', 'Apprenticeships/Internship/Volunteer ')
)


class OpeningDetails(models.Model):
    company = models.ForeignKey(CompanyProfile)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True, null=True, choices=INDUSTRY_CHOICES)
    job_type = models.CharField(max_length=100, blank=True, null=True, choices=JOB_TYPE)
    job_description = models.TextField(blank=True, null=True,)
    job_location = models.CharField(max_length=100)
    job_start_date = models.DateTimeField()
    #job_end_date = models.DateTimeField()
    job_profile = models.TextField(blank=True, null=True,)
    salary_min = models.CharField(max_length=100, blank=True, null=True, choices=MIN_EXPERINCE)
    salary_max = models.CharField(max_length=100, blank=True, null=True, choices=MAX_EXPERINCE)
    created_at = models.DateTimeField(auto_now_add=True)

    #Keywords = models.TextField()
    # work_experienc_min = models.CharField(max_length=100, choices=MIN_EXPERINCE)
    # work_experienc_max = models.CharField(max_length=100, choices=MAX_EXPERINCE)
    # annual_ctc_min = models.CharField(max_length=100)
    # annual_ctc_max = models.CharField(max_length=100)
    # number_of_vacancies = models.CharField(max_length=100, choices=NO_OPENINGS)
    # industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    # functional_area = models.CharField(max_length=100, choices=FUNCTIONAL_AREA_CHOICES)
    # job_role = models.TextField()
    # qualifications = models.CharField(max_length=100, choices=QUALIFICATIONS)
    # skill = models.CharField(max_length=100)
    # contact_number = models.CharField(max_length=100, null=True, blank=True)
    # contact_email = models.CharField(max_length=100)
    # active_status = models.BooleanField(default=True)






