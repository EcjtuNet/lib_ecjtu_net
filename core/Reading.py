#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Request import Request
from Model import *

class Reading(db.Entity):

    user = Set("User")
    name = Required(str)
    code = Required(str)
    borrow_time = Required(str)
    return_time = Required(str)
    renewed = Required(bool)
    renew_link = Required(str)
    index_code = Required(str)
    address = Required(str)

    def renew(self):
        Request().get(self.rewew_link)
