# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_login', '0002_remove_userprofile_curr_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='curr_booking',
            field=models.CharField(blank=True, default=b'', max_length=19),
        ),
    ]
