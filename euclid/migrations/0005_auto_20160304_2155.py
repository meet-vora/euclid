# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euclid', '0004_remove_question_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='questions_solved',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
