# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]