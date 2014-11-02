#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page.Request import Request
from Model import *

class Reading(db.Entity):

    user = Set("User")
    name = Required(str)
    code = Required(str) #Such as 1420149
    borrow_time = Required(str)
    due_time = Required(str)
    renewed = Required(bool)
    renew_link = Required(str)
    index_code = Required(str) #Such as TP368.5/A114
    address = Required(str)

    def renew(self):
        Request().get(self.rewew_link)
