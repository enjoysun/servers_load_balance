#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/8/15 下午11:02
# @Author  : YouMing
# @Email   : myoueva@gmail.com
# @File    : platform_service.py
# @Software: PyCharm
from commond.zoohandler import ServiceDiscovery
from commond.balancestrategy import Round_Robin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


class ServiceList(APIView):
    """
    services handler
    """
    def get(self, request):
        server_path = self.request.query_params.get('path', None)
        host_ip = ServiceDiscovery().endpoint_service(server_path)
        result = dict(data=host_ip)
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        pass


@api_view(['GET'])
def collect_server(request):
    handler = ServiceDiscovery()
    handler.service_repository('/Service')
    return Response(status=status.HTTP_200_OK)
