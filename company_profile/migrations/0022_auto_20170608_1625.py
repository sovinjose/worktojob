# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-08 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0021_auto_20170608_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobprofile',
            name='industry_exp_months',
        ),
        migrations.RemoveField(
            model_name='jobprofile',
            name='work_experience_months',
        ),
    ]
