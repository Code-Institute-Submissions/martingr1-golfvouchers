# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-15 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200415_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='manufacturer',
            field=models.CharField(blank=True, default='manufacturer', max_length=25, null=True),
        ),
    ]