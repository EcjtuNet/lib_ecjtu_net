#!/usr/bin/env python
# -*- coding: utf-8 -*-
from UserPage import UserPage
from Page import Page
from Request import Request
from HistoryParser import HistoryParser 

class HistoryPage(Page):
	def __init__(self,username,password=''):
		self.parser = HistoryParser()
		self.page = 1
		self.username = username
		self.password = password

	def fetchHtml(self):
		login_url = 'http://lib.ecjtu.jx.cn/gdweb/ReaderTable.aspx'
		history_url = 'http://lib.ecjtu.jx.cn/gdweb/HisdoryList.aspx?PageNo='+str(self.page)
		r = Request()
		r.setCookie(self.username,self.password).get(login_url)
		self._html = r.get(history_url)
		return self

if __name__ == "__main__":
	history = HistoryPage(20132110010311)
	print history.fetchHtml().html()
	print history.parseHtml()
