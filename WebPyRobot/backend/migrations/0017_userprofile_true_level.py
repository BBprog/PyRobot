# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_battlehistory_map_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='true_level',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
