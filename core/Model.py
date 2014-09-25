#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Database import Database

class Model:
	def __init__(self, main_id=''):
		self.data = {}
		self.database = Database(True)
		if main_id: 
                        self.data = self.getBy(self.main_id_name, main_id)

	def save(self):
		pass

	def getByUid(self):
		pass

	def set(self, key, value):
		self.data[key] = value
		return self

	def get(self, key):
		return self.data[key]

	def setData(self, dict_data):
		for i in dict_data:
			self.data[i] = dict_data[i]
		return self

        def getBy(self, key, value):
                self.database.cursor.execute('SELECT * FROM '+str(self.table)+' WHERE '+str(key)+'='+str(value))
                return self.database.cursor.fetchone()
