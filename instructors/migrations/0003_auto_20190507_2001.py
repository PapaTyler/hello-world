# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_instructor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
