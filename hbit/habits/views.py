# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from habits.models import Habit
from actions.forms import ActionForm


class HabitListView(ListView):
    model = Habit

    def get_queryset(self):
        qs = super(HabitListView, self).get_queryset()
        return qs.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(HabitListView, self).get_context_data(**kwargs)
        context['form'] = ActionForm()
        return context
