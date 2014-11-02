#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pony.orm import *

sys.path.append("..")
import Config

if Config.get('develop') == True:
    db = Database('sqlite', 'test.sqlite', create_db=True)
    sql_debug(True)
else:
    db = Database('mysql', host=Config.get('host'), user=Config.get('user'), passwd=Config.get('passwd'), db=Config.get('db'))

from User import *
from History import *
from Token import *
from Reading import *

db.generate_mapping(create_tables=True)
