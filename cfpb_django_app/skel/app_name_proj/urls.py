# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^{{app_name}}', include('{{app_name}}.urls')),
]
