# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 11:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Tip: use an emoji!', max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('target', models.PositiveIntegerField(blank=True, null=True)),
                ('period', models.PositiveIntegerField(blank=True, choices=[(0, 'daily'), (1, 'weekly'), (2, 'monthly')], null=True)),
                ('positive', models.BooleanField(default=True, help_text='I want to do more of this')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
