# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from firstTest.models import Event, Guest

# Registeryour models here.
# admin.site.register(Event)
# admin.site.register(Guest)

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    list_filter = ['status']      # 过滤器
    search_fields = ['name']      # 搜索栏


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
    list_filter = ['sign']                 # 过滤器
    search_fields = ['realname','phone']   # 搜索栏

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
