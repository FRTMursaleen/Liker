# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-11 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter_Bot', '0011_accounts_data_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts_data',
            name='user',
        ),
    ]
