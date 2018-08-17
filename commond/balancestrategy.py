#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/8/16 下午3:49
# @Author  : YouMing
# @Email   : myoueva@gmail.com
# @File    : balancestrategy.py
# @Software: PyCharm
from itertools import *


class Round_Robin(object):
    def __init__(self, *args, **kwargs):
        super(Round_Robin, self).__init__(*args, **kwargs)

    def round_robin(self, server_lst, cur=[0]):
        length = len(server_lst)
        ret = server_lst[cur[0] % length]
        cur[0] = (cur[0] + 1) % length
        return ret

    7

    def weight_round_robin(self, servers, cur=[0]):
        weighted_list = []
        for k, v in servers.iteritems():
            weighted_list.extend([k] * v)
        length = len(weighted_list)
        ret = weighted_list[cur[0] % length]
        cur[0] = (cur[0] + 1) % length
        return ret


if __name__ == "__main__":
    rr_obj = Round_Robin()
    for i in range(50):
        print(rr_obj.round_robin(['a', 'b', 'c']))


