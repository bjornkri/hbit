# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from actions.models import Action


class ActionListView(ListView):
    model = Action
