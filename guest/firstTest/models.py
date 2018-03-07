# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 发布会表格
class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)
#   处理中文字符 如果python3为__str__()    python2 为 __unicode__()
    def __unicode__(self):
        return self.name

class Guest(models.Model):
    event = models.ForeignKey(Event)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("event", "phone")

#   处理中文字符 如果python3为__str__()    python2 为 __unicode__()
    def __unicode__(self):
        return self.realname
