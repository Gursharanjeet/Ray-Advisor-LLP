# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-15 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeDashboard', '0001_initial'),
        ('AdminDashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackemployee',
            name='reason',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ereason', to='EmployeeDashboard.ReportWork'),
        ),
        migrations.AddField(
            model_name='trackemployee',
            name='report_date',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='rdate', to='EmployeeDashboard.ReportWork'),
        ),
        migrations.AddField(
            model_name='trackemployee',
            name='work_progress',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='wprogress', to='EmployeeDashboard.ReportWork'),
        ),
        migrations.AddField(
            model_name='workassign',
            name='emp_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EmployeeDashboard.EmployeeProfile'),
        ),
    ]
