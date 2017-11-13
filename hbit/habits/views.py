# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from habits.models import Habit


class HabitListView(ListView):
    model = Habit
