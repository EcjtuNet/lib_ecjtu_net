#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
        'salt' : 'salt',
        'token_expire' : 3600,#second
        'host' : '127.0.0.1',
        'user' : '',
        'passwd' : '',
        'db' : '',
        'charset' : 'utf8'
        }
def get(str):
    return config[str]
