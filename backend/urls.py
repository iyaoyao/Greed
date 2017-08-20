#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YaoYao"
# Date: 2017/8/20

from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
