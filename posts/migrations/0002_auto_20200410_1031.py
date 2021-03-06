# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-10 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='post',
            name='initial_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
