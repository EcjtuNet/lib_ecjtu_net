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
    'develop' : True
}
def get(str):
    return config[str]
