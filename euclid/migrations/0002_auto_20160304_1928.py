# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('euclid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='euclid.UserProfile', unique=True),
        ),
    ]
