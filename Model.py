#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pony.orm import *
from Page.Request import Request
import Config
import hashlib
import time

if Config.get('develop') == True:
    db = Database('sqlite', 'test.sqlite', create_db=True)
    sql_debug(True)
else:
    db = Database('mysql', host=Config.get('host'), user=Config.get('user'), passwd=Config.get('passwd'), db=Config.get('db'))

class User(db.Entity):
    name = Optional(str)
    password = Optional(str)
    student_id = Required(str, unique=True)
    email = Optional(str, unique=True)
    reg_time = Required(str)
    renew_flag = Optional(bool)
    tokens = Set(lambda: Token)
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
    def login(cls, username, password):
        u = User.get(student_id=username, password=User._salt(username, password))
        u._setToken()
        return u
    
    @classmethod
    def register(cls, username, password):
        return User(
                name=username, 
                student_id=username, 
                password=User._salt(username, password), 
                reg_time=str(int(time.time()))
                )
   
    @classmethod
    def is_exist(cls, username):
        return User.get(student_id=username) 
        
    def _setToken(self):
        self.token = self.tokens.create(token=User._makeToken(self.student_id), last_use_time=str(int(time.time())))

    def checkToken(self, token):
        token = Token.get(token=token)
        if token and self==token.user:
            if int(time.time()) - int(token.last_use_time) < Config.get('token_expire'):
                token.last_use_time = str(int(time.time()))
                return True
        return False

    @classmethod
    def _salt(self, username, password):
        return password #!!!
        return hashlib.sha256(str(username) + \
                str(hashlib.sha256(str(password)+str(Config.get('salt'))).hexdigest())).hexdigest()

    @classmethod
    def _makeToken(self, username):
        return str(hashlib.md5(str(username)+str(int(time.time()))).hexdigest())

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

class Token(db.Entity):
    user = Required(User)
    token = Required(str)
    last_use_time = Required(str)

db.generate_mapping(create_tables=True)
