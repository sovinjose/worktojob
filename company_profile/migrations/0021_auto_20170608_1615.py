# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-08 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0020_auto_20170529_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobprofile',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobprofile',
            name='job_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
