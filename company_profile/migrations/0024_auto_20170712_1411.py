# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0023_auto_20170712_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobprofile',
            name='salary_max',
            field=models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobprofile',
            name='salary_min',
            field=models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], default=3, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobprofile',
            name='salary_type',
            field=models.CharField(choices=[('Per Annum', 'Per Annum'), ('Per Hour', 'Per Hour')], default=3, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobprofile',
            name='work_experience_year',
            field=models.CharField(choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19')], default=4, max_length=100),
            preserve_default=False,
        ),
    ]
