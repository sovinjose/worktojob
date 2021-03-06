# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-09 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0002_auto_20170406_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('IT-Software / Software Services', 'IT-Software / Software Services'), ('BPO / Call Centre / ITES', 'BPO / Call Centre / ITES'), ('Automobile / Auto Anciliary / Auto Components', 'Automobile / Auto Anciliary / Auto Components'), ('Accounting / Finance', 'Accounting / Finance'), ('Advertising / PR / MR / Event Management', 'Advertising / PR / MR / Event Management'), ('Agriculture / Dairy', 'Agriculture / Dairy'), ('Animation / Gaming', 'Animation / Gaming'), ('Architecture / Interior Design', 'Architecture / Interior Design'), ('Aviation / Aerospace Firms', 'Aviation / Aerospace Firms'), ('Banking / Financial Services / Broking', 'Banking / Financial Services / Broking'), ('Brewery / Distillery', 'Brewery / Distillery'), ('Broadcasting', 'Broadcasting'), ('Consumer Electronics / Appliances / Durables', 'Consumer Electronics / Appliances / Durables'), ('Education / Teaching / Training', 'Education / Teaching / Training'), ('Electricals / Switchgears', 'Electricals / Switchgears'), ('Others', 'Others')], max_length=100)),
                ('job_type', models.CharField(choices=[('Fulltime/Part-time', 'Fulltime/Part-time'), ('Permanent/Temporary/Contract', 'Permanent/Temporary/Contract'), ('Apprenticeships/Internship/Volunteer ', 'Apprenticeships/Internship/Volunteer ')], max_length=100)),
                ('job_description', models.TextField()),
                ('job_location', models.CharField(max_length=100)),
                ('job_start_date', models.DateTimeField()),
                ('salary_min', models.CharField(blank=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], max_length=100, null=True)),
                ('salary_max', models.CharField(blank=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_profile.CompanyUserProfile')),
            ],
        ),
    ]
