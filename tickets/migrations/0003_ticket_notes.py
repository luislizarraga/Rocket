# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20161109_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
