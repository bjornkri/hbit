# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.views.generic import ListView, CreateView

from actions.models import Action


class ActionListView(ListView):
    model = Action


class ActionCreateView(CreateView):
    model = Action
    fields = ['description']
    success_url = '/'

    def form_valid(self, form):
        action = form.save(commit=False)
        action.habit_id = self.kwargs['habit_pk']
        action.save()
        messages.info(self.request, "{} created!".format(action.habit.code))
        return super(ActionCreateView, self).form_valid(form)
