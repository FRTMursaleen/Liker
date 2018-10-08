# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-11 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter_Bot', '0002_favouritekeywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestrictedKeywords',
            fields=[
                ('Res_key_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Restrited_keywords', models.CharField(max_length=100, null=True, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
