# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0011_auto_20170424_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(max_length=40),
        ),
    ]
