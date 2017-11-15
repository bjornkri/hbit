# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, CreateView

from actions.models import Action


class ActionListView(ListView):
    model = Action


class ActionCreateView(CreateView):
    model = Action
    fields = ['description']
    success_url = '/'

    def form_valid(self, form):
        f = form.save(commit=False)
        f.habit_id = self.kwargs['habit_pk']
        f.save()
        return super(ActionCreateView, self).form_valid(form)
