# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import redirect
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
        if action.habit.user == self.request.user:
            action.save()
            desc = ""
            if action.description:
                desc = " ({})".format(action.description)
            messages.info(
                self.request, "{}{} created!".format(action.habit.code, desc))
        else:
            messages.error(
                self.request, "Trying to do someone else's hBIT!")
            return redirect('home')
        return super(ActionCreateView, self).form_valid(form)
