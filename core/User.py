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

    def save(self):
        pass

    def login(self, username, password):
        self.database.cursor.execute(
            'SELECT * FROM user '+
            'WHERE student_id=\''+username+'\''+
            ' AND password=\''+self._salt(username, password)+'\''
        )
        row = self.database.cursor.fetchone()
        if row:
            u = User(row['uid'])
            u.setData(row)
            u.token = self._makeToken(username)
            u._setToken()
            return u
        else:
            return False        

    def register(self, username, password):
        if self.is_exist(username):
            return False
        result = self.database.cursor.execute(
            'INSERT INTO user(student_id, password, reg_time) VALUES(%s,%s,%s)',
            (username,self._salt(username, password),str(int(time.time())))
        )
        if result:
            self.database.conn.commit()
            return username
        return False
   
    def is_exist(self, username=False):
        if not username:
            if not self.data['student_id']:
                return False
            username = self.data['student_id']
        self.database.cursor.execute(
            'SELECT * FROM user WHERE student_id=\''+username+'\''
        )
        row = self.database.cursor.fetchone()
        if row:
            return True
        return False

    def _setToken(self):
        self.database.cursor.execute(
            'INSERT INTO token VALUES ('+
                str(self.data['uid'])+',\''+
                str(self.token)+'\','+
                str(int(time.time()))+
            ')'
            )
        self.database.conn.commit()

    def checkToken(self, token):
        self.database.cursor.execute(
            'SELECT * FROM token WHERE '+
            'uid='+self.data['uid']+
            ' AND token=\''+token+'\''
        )
        row = self.database.cursor.fetchone()
        if row:
            if int(time.time()) - int(row['last_use_time']) < Config.get('token_expire'):
                self.database.cursor.execute(
                    'UPDATA token SET last_use_time='+time.time()+
                    ' WEHERE uid='+self.data['uid']+
                    ' AND token=\''+token+'\''
                )
                self.database.conn.commit()
                return true
        return false

    def _salt(self, username, password):
        return hashlib.sha256(str(username) + \
                str(hashlib.sha256(str(password)+str(Config.get('salt'))).hexdigest())).hexdigest()

    def _makeToken(self, username):
        return str(hashlib.md5(str(username)+str(int(time.time()))).hexdigest())
