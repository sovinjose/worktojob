# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-09 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0008_companyuserprofile_compant_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyuserprofile',
            old_name='compant_size',
            new_name='company_size',
        ),
    ]
