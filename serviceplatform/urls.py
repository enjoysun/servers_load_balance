#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/8/15 下午11:04
# @Author  : YouMing
# @Email   : myoueva@gmail.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import platform_service

urlpatterns = [
    url(r'services/', platform_service.ServiceList.as_view(), name='services_handler'),
    url(r'collect/', platform_service.collect_server, name='init'),
]


