# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_auto_20171113_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
