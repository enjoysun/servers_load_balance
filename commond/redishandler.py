#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/8/16 上午11:54
# @Author  : YouMing
# @Email   : myoueva@gmail.com
# @File    : redishandler.py
# @Software: PyCharm
import os
from redis import Redis

REDIS_HOST = os.environ.get('REDIS_HOST', 'service_redis')
REDIS_PASS = os.environ.get('REDIS_PASS', '123')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_DB = os.environ.get('REDIS_DB', 1)


class RedisDB(object):
    """
    Redis 接口
    """

    def __init__(self, db=None, decode_responses=True):
        db = db if db else REDIS_DB
        self.RD = Redis(host=REDIS_HOST, db=db, password=REDIS_PASS, port=REDIS_PORT, decode_responses=decode_responses)

    def exist(self, key):
        return self.RD.exists(key)

    def set(self, name, value, ex):
         return self.RD.set(name=name, value=value, ex=ex)

    def del_key(self, key):
        return self.RD.delete(key)

    def get(self, name):
        return self.RD.get(name=name)

    def hset(self, name, key, value):
        return self.RD.hset(name=name, key=key, value=value)

    def hget(self, name, key):
        return self.RD.hget(name=name, key=key)

    def hget_all(self, name):
        return self.RD.hgetall(name=name)

    def hmset(self, name, mapping):
        return self.RD.hmset(name=name, mapping=mapping)

    def hmget(self, name, keys):
        return self.RD.hmget(name=name, keys=keys)

    def zadd(self, name, *args, **kwargs):
        """
        As *args, in the form of: name1, score1, name2, score2, ...(the official Redis
        command expects score1, name1, score2, name2.)
        or as **kwargs, in the form of: name1=score1, name2=score2, ...
        """
        return self.RD.zadd(name, *args, **kwargs)

    def zrange(self, name, start, end, withscores=True):
        return self.RD.zrange(name=name, start=start, end=end, withscores=withscores)

    def zrangebyscore(self, name, score_min, score_max, start=None, num=None,
                      withscores=False, score_cast_func=float):

        return self.RD.zrangebyscore(name, min=score_min, max=score_max, start=start, num=num,
                                     withscores=withscores, score_cast_func=score_cast_func)

    def zscore(self, name, value):
        return self.RD.zscore(name=name, value=value)

    def lpush(self, key, value):
        return self.RD.lpush(key, value)

    def llen(self, name):
        return self.RD.llen(name=name)

    def lrange(self, name, start, end):
        return self.RD.lrange(name=name, start=start, end=end)

    def keys(self, key):
        return self.RD.keys(key)


