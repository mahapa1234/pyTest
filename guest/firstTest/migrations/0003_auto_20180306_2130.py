# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTest', '0002_auto_20180306_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]