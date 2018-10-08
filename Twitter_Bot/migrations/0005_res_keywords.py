# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-11 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter_Bot', '0004_fav_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Res_Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Twitter_Bot.Accounts_Data')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Twitter_Bot.RestrictedKeywords')),
            ],
        ),
    ]
