#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Model import *
from History import History
from Reading import Reading
from Token import Token
import hashlib
import time

class User(db.Entity):

    name = Optional(str)
    password = Optional(str)
    student_id = Required(str, unique=True)
    email = Optional(str, unique=True)
    reg_time = Required(str)
    renew_flag = Optional(bool)
    tokens = Set(Token)
    readings = Set(Reading)
    histories = Set(History)

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
        token = self.tokens.get(token=token)
        if token:
            if int(time.time()) - int(token.last_use_time) < Config.get('token_expire'):
                token.last_use_time = time.time()
                return true
        return false

    @classmethod
    def _salt(self, username, password):
        return password #!!!
        return hashlib.sha256(str(username) + \
                str(hashlib.sha256(str(password)+str(Config.get('salt'))).hexdigest())).hexdigest()

    @classmethod
    def _makeToken(self, username):
        return str(hashlib.md5(str(username)+str(int(time.time()))).hexdigest())
