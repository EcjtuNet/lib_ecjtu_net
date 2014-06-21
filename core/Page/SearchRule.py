#!/usr/bin/env python
# -*- coding: utf-8 -*-
#简单实现了组合查询，需修改

class SearchRule:
	def __init__(self):
		self.rule = {}
		self.ruleTable = {
			'title' : 'DropScarchKay1',
			'author' : 'DropScarchKay2'
		}
	def add(self, key, value):
		if key in self.ruleTable:
			self.rule[self.ruleTable[key]] = value
	def make(self):
		return self.rule