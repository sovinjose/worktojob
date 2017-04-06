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