# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-20 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter_Bot', '0019_auto_20180619_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='black_user',
            name='black_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Twitter_Bot.Black_List_Names', unique=True),
        ),
    ]
