# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-19 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0024_auto_20170712_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('send invitation', 'send invitation'), ('invitation accepted', 'invitation accepted')], default='available', max_length=100),
        ),
    ]
