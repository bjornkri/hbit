# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Habit(models.Model):
    DAILY, WEEKLY, MONTHLY = range(3)
    PERIOD_CHOICES = (
        (DAILY, 'daily'),
        (WEEKLY, 'weekly'),
        (MONTHLY, 'monthly'),
    )
    code = models.CharField(
        max_length=10,
        help_text='Tip: use an emoji!')
    description = models.TextField(blank=True, null=True)
    target = models.PositiveIntegerField(blank=True, null=True)
    period = models.PositiveIntegerField(choices=PERIOD_CHOICES, default=DAILY)
    positive = models.BooleanField(
        default=True, help_text='I want to do more of this')
    user = models.ForeignKey(User)

    def __str__(self):
        return "<{}: {}>".format(self.code, self.user)
