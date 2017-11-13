# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from habits.models import Habit


class Action(models.Model):
    habit = models.ForeignKey(Habit)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} on {}".format(self.habit, self.timestamp)
