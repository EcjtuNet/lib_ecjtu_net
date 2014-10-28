#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Model import *
from History import History
from Reading import Reading
from Token import Token
import hashlib
import time

class User(db.Entity):

    name = Required(str)
    password = Required(str)
    student_id = Required(str, unique=True)
    email = Required(str, unique=True)
    reg_time = Required(str)
    renew_flag = Required(str)
    tokens = Set(Token)
    readings = Set(Reading)
    histories = Set(History)

    def allRenew(self):
        with db_session:
            read_list = self.readings
            for i in read_list:
    	        i.renewed = True

    @classmethod
    def login(cls, username, password):
        with db_session:
            return User.get(student_id=username, password=User._salt(username, password))
    
    @classmethod
    def register(cls, username, password):
        with db_session:
            return User(student_id=username, password=User._salt(username, password), reg_time=str(int(time.time())))
   
    @classmethod
    def is_exist(cls, username):
        with db_session:
            return User(student_id=username) 
        
    def _setToken(self):
        with db_session:
            self.tokens.create(token=User._makeToken(self.student_id), last_use_time=str(int(time.time())))

    def checkToken(self, token):
        with db_session:
            token = self.tokens.get(token=token)
            if token:
                if int(time.time()) - int(token.last_use_time) < Config.get('token_expire'):
                    token.last_use_time = time.time()
                    return true
            return false

    @classmethod
    def _salt(self, username, password):
        return hashlib.sha256(str(username) + \
                str(hashlib.sha256(str(password)+str(Config.get('salt'))).hexdigest())).hexdigest()

    @classmethod
    def _makeToken(self, username):
        return str(hashlib.md5(str(username)+str(int(time.time()))).hexdigest())
