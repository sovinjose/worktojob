# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-08 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0004_auto_20170308_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='openingdetails',
            name='skill',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openingdetails',
            name='job_role',
            field=models.TextField(),
        ),
    ]