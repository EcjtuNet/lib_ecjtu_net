#!/usr/bin/env python
# -*- coding: utf-8 -*-
from History import History
from Reading import Reading
from Database import Database
from Model import Model

class User():
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
