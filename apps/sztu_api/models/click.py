# -*- coding:utf-8 -*-
from datetime import datetime

from django.utils import timezone

__author__ = 'zhoujifeng'
__date__ = '2019/3/8 13:30'

from django.db import models


class Click(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.CharField(max_length=255)
    dom_name = models.CharField(max_length=64)
    url = models.CharField(max_length=800, blank=True, null=True)
    access_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    update_time = models.DateTimeField('最后修改时间', auto_now=True)

