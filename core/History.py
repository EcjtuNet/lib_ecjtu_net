#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Model import *
from User import *

class History(db.Entity):

    user = Set("User")
    name = Required(str)
    code = Required(str)
    time = Required(str)
    type = Required(str)

