# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-11 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter_Bot', '0009_tweetsdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Black_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Twitter_Bot.Accounts_Data')),
                ('black_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Twitter_Bot.Black_List_Names')),
            ],
        ),
    ]
