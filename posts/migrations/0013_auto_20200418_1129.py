# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-18 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200418_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, choices=[('sale', 'Sale')], max_length=25, null=True),
        ),
    ]
