# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import ListView

from habits.models import Habit
from actions.models import Action
from actions.forms import ActionForm


class HabitListView(LoginRequiredMixin, ListView):
    model = Habit

    def get_queryset(self):
        qs = super(HabitListView, self).get_queryset()
        return qs.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(HabitListView, self).get_context_data(**kwargs)
        context['form'] = ActionForm()
        context['todays_actions'] = Action.objects.filter(
            habit__user=self.request.user,
            timestamp__date=timezone.now()
        )
        return context
