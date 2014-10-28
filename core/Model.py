#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pony.orm import *
sys.path.append("..")
import Config

if Config.get('develop') == True:
    db = Database('sqlite', 'test.sqlite', create_db=True)
else:
    db = Database('mysql', host=Config.get('host'), user=Config.get('user'), passwd=Config.get('passwd'), db=Config.get('db'), create_db=True)
