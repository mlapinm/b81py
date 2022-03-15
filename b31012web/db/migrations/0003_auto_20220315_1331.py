# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-15 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20220315_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='subscribers',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='author',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
