#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'salt' : 'salt',
    'token_expire' : 3600,#second
    'host' : '202.101.208.35',
    'user' : 'lib_ecjtu_net',
    'passwd' : 'V9buaZsGC83Wtdb9',
    'db' : 'lib_ecjtu_net',
    'charset' : 'utf8',
    'develop' : True,
    'auto_renew_time' : 3 * 24 * 60 * 60, #second
    'lib_base_url' : 'http://lib.ecjtu.jx.cn/gdweb/',
    'redis_host' : 'localhost',
    'redis_port' : '6379',
    'redis_db' : 0
}
def get(str):
    return config[str]
