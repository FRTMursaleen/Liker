# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-07 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter_Bot', '0022_auto_20180622_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouritekeywords',
            name='num_limits',
        ),
    ]
