# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-10 10:46
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0010_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyuserprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='banner',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='static/profile_pic/'), upload_to='cmpny_banner'),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='contact_details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='contact_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='linkedIn',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='long_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='mission',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuserprofile',
            name='vision',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyuserprofile',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='static/profile_pic/'), upload_to='cmpny_logo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='static/profile_pic/'), upload_to='%Y-%m-%d'),
        ),
    ]
