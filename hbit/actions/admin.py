# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from actions.models import Action


class ActionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Action, ActionAdmin)
