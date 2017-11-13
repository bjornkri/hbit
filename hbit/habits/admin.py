# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from habits.models import Habit


class HabitAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'positive', 'target', 'period']


admin.site.register(Habit, HabitAdmin)
