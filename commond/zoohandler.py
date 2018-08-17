#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/8/16 上午11:39
# @Author  : YouMing
# @Email   : myoueva@gmail.com
# @File    : zoohandler.py
# @Software: PyCharm
import os
import logging

from kazoo.client import KazooClient, KazooState
from commond.redishandler import RedisDB
from commond.balancestrategy import Round_Robin

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(pathname)s %(funcName)s%(lineno)d %(levelname)s: %(message)s'
)


class ServiceDiscovery(object):
    """
    服务中心
    """
    def __init__(self):
        """初始化zk客户端，一个客户端可以指定多台zookeeper地址"""
        zk_host = os.environ.get('ZK_HOST', '0.0.0.0')
        # zk_port = os.environ.get('ZK_PORT', '2181')
        self.zk_client = KazooClient(hosts='zookeeper_1:2181,zookeeper_2:2182,zookeeper_3:2183'.format(zk_host), timeout=10.0, logger=logging)
        self.zk_client.start()
        self.state = self.zk_client.add_listener(self.client_listener)
        self.redis_client = RedisDB()

    def service_repository(self, znode):
        """服务信息中心 key:service:znode-path"""
        data, stat = self.zk_client.get(znode)
        childrens = self.zk_client.get_children(znode)
        if not len(childrens) > 0:
            self.redis_client.set("service:{0}".format(znode), data)
        while len(children) > 0:
            for children in childrens:
                path = ''
                if children != '/':
                    path = '{0}/{1}'.format(znode, children)
                else:
                    path = '/{0}'.format(children)
                self.service_repository(path)

    def client_listener(self, state):
        """监控连接状态"""
        if state == KazooState.LOST:
            return dict(state='LOST', result=False)
        elif state == KazooState.SUSPENDED:
            return dict(state='SUSPENDED', result=False)
        else:
            return dict(state='CONNECTED', result=True)

    def create_service(self, znode, data):
        """data require b"""
        return self.zk_client.create(znode, data, ephemeral=True, sequence=True)

    def create_ensure(self, znode):
        return self.zk_client.ensure_path(znode)

    def endpoint_service(self, servername):
        keys = self.redis_client.keys(r'{0}/*'.format(servername))
        znode = Round_Robin().round_robin(keys)
        return self.redis_client.get(znode)

zk = ServiceDiscovery()


@zk.zk_client.ChildrenWatch('/Service/User')
def watch_children(childrens):
    """监控节点数据"""
    for children in childrens:
        children = '/Service/User/{0}'.format(children)
        if zk.zk_client.exists(children):
            data, stat = zk.zk_client.get(children)
            if stat:
                zk.redis_client.set('service:{0}'.format(children), data, None)
            else:
                zk.redis_client.delete('service:{0}'.format(children))
        else:
            if zk.redis_client.exists(children):
                zk.redis_client.delete('service:{0}'.format(children))








