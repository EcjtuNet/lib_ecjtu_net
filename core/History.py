#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Model import Model
from Database import Database

class History(Model):
	def __init__(self, hid=''):
		self.table = 'history'
		self.main_id_name = 'hid'
		Model.__init__(self, hid)

	def getByUid(self, uid):
		self.database.cursor.execute('SELECT * FROM '+self.table+' WHERE uid='+int(uid))
		history_list = []
		for i in self.database.cursor.fetchall():
			history_list.append(History().setData(i))

	def save(self):
		self.database.cursor.execute(
			'INSERT INTO '+self.table+'(`uid`, `name`, `code`, `time`, `type`) VALUES('+
				self.data['uid']+','+
				self.data['name']+','+
				self.data['code']+','+
				self.data['time']+','+
				self.data['type']+','+
			')'
		)