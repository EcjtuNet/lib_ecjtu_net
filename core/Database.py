#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import MySQLdb
import Config

class Database:
	def __init__(self, dict_result=False):
		self.conn=MySQLdb.connect(host=Config.get('host'),user=Config.get('user'),passwd=Config.get('passwd'),db=Config.get('db'),charset=Config.get('charset'))  
		self.cursor = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) if dict_result else self.conn.cursor()
