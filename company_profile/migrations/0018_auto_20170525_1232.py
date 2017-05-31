# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-25 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0017_jobprofile_tech_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobprofile',
            name='tech_skills',
        ),
        migrations.AlterField(
            model_name='jobprofile',
            name='certifications',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='techskill',
            name='job_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_profile.JobProfile'),
        ),
    ]
