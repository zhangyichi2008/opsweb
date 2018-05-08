# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-25 10:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('code_release', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deploy',
            name='applicant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL, verbose_name='\u7533\u8bf7\u4eba'),
        ),
        migrations.AlterField(
            model_name='deploy',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL, verbose_name='\u6307\u6d3e\u4eba'),
        ),
    ]
