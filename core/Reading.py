#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Model import Model
from Database import Database
from Page.Request import Request

class Reading(Model):
	def __init__(self, rid=''):
		self.table = 'reading'
		self.main_id_name = 'rid'
		Model.__init__(self, rid)

	def getByUid(self, uid):
		self.database.cursor.execute('SELECT * FROM '+self.table+' WHERE uid='+int(uid))
		history_list = []
		for i in self.database.cursor.fetchall():
			history_list.append(Reading().setData(i))

	def save(self):
		self.database.cursor.execute(
			'INSERT INTO '+self.table+
				'(`uid`, `name`, `code`, `borrow_time`, `return_time`, '+
					'`renewed`, `renew_link`, `index_code`, `address`)'+
			' VALUES('+
				self.data['uid']+','+
				self.data['name']+','+
				self.data['code']+','+
				self.data['borrow_time']+','+
				self.data['return_time']+','+
				self.data['renewed']+','+
				self.data['renew_link']+','+
				self.data['index_code']+','+
				self.data['address']+','+
			')'
		)

	def renew(self):
			Request().get(self.data['rewew_link'])
