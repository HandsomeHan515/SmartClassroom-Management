# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 13:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_auto_20170607_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to=settings.AUTH_USER_MODEL),
        ),
    ]
