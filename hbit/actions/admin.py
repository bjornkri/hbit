# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from actions.models import Action


class ActionAdmin(admin.ModelAdmin):
    list_display = ['get_code', 'get_user', 'timestamp', 'description']
    search_fields = ['habit__description', 'habit__user__username',
                     'description', 'habit__code']

    def get_user(self, obj):
        return obj.habit.user
    get_user.short_description = 'User'
    get_user.admin_order_field = 'habit__user'

    def get_code(self, obj):
        return obj.habit.code
    get_code.short_description = 'Code'
    get_code.admin_order_field = 'habit__code'


admin.site.register(Action, ActionAdmin)
