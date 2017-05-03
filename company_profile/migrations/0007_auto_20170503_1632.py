# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-03 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0006_employe_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobprofile',
            name='end_date',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='start_date',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
