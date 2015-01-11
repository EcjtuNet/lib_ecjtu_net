#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pony.orm import *
from Page.Request import Request
import Config
import hashlib
import time
from UserCenter import UserCenter

if Config.get('develop') == True:
    db = Database('sqlite', 'test.sqlite', create_db=True)
    sql_debug(True)
else:
    db = Database('mysql', host=Config.get('host'), user=Config.get('user'), passwd=Config.get('passwd'), db=Config.get('db'))

class User(db.Entity):
    name = Optional(str)
    student_id = Required(str, unique=True)
    renew_flag = Optional(bool)
    readings = Set(lambda: Reading)
    histories = Set(lambda: History)

    def allRenew(self):
        read_list = self.readings
        for i in read_list:
            i.renewed = True

    @classmethod
    def getBySid(cls, student_id):
        return User.get(student_id=student_id)

    @classmethod
    def checkToken(cls, username, token):
        u = UserCenter.User()
        u.username = username
        u.token = token
        if not u.checkToken():
            return False
        u = User.getBySid(username)
        return u
  
    @classmethod
    def is_exist(cls, username):
        return User.get(student_id=username) 
        
class History(db.Entity):
    user = Required(User)
    name = Required(str)
    code = Required(str)
    time = Required(str)
    type = Required(str)

class Reading(db.Entity):
    user = Required(User)
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

db.generate_mapping(create_tables=True)
