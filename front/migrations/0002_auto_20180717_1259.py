# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-17 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
