#!/usr/bin/env python
# -*- coding: utf-8 -*-
from History import History
from Reading import Reading
from Database import Database
from Model import Model
import Config
import hashlib
import time

class User(Model):
    def __init__(self, uid=''):
    	self.table = 'user'
        self.main_id_name = 'uid'
    	Model.__init__(self, uid)

    def getHistory(self):
	return History().getByUid(self.data[self.main_id_name])
	
    def getReading(self):
	return Reading().getByUid(self.data[self.main_id_name])

    def allRenew(self):
	read_list = Reading().getByUid(self.data[self.main_id_name])
        for i in read_list:
    	    i.Reading().renew()

    def login(self, username, password):
        self.database.cursor.execute(
            'SELECT * FROM user '+
            'WHERE student_id='+username+
            ' AND password='+self._salt(username, password)
        )
        row = self.database.cursor.fetchone()
        if row:
            u = User(row['uid'])
            u.setData(row)
            u.token = self._makeToken(username)
            u._setToken()
            return u
        else:
            return false

    def _setToken(self):
        self.database.cursor.execute(
            'INSERT INTO token VALUES ('+
                self.data['uid']+','+
                self.token+','+
                str(time.time())+
            ')'
            )

    def checkToken(self, token):
        self.database.cursor.execute(
            'SELECT * FROM token WHERE '+
            'uid='+self.data['uid']+
            ' AND token='+token
        )
        row = self.database.cursor.fetchone()
        if row:
            if time.time() - row['last_use_time'] < Config.get('token_expire'):
                self.database.cursor.execute(
                    'UPDATA token SET last_use_time='+time.time()+
                    ' WEHERE uid='+self.data['uid']+
                    ' AND token='+token
                )
                return true
        return false

    def _salt(self, username, password):
        return hashlib.sha256(str(username) + \
                str(hashlib.sha256(str(password)+str(Config.get('salt')))))

    def _makeToken(self, username):
        return str(hashlib.md5(str(username)+str(time.time())))
