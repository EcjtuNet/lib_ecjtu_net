#!/usr/bin/env python
# -*- coding: utf-8 -*-
from UserPage import UserPage
from Page import Page
from Request import Request
from bs4 import BeautifulSoup
from HistoryParser import HistoryParser 

class HistoryPage(Page):
	def __init__(self,username,password=''):
		self.parse = HistoryParser()
		self.page = 1
		self.username = username
		self.password = password

	def fetchPage(self):
		login_url = 'http://lib.ecjtu.jx.cn/gdweb/ReaderTable.aspx'
		history_url = 'http://lib.ecjtu.jx.cn/gdweb/HisdoryList.aspx?PageNo='+str(self.page)
		r = Request()
		self._html = r.setCookie(self.username,self.password).get(login_url)
		self._result = r.get(history_url)
		return self

	def nextpage(self):
		self.page += 1
		return self

	def matchpage(self):
		soup = BeautifulSoup(self._result)
		tag = soup.font
		return tag

if __name__ == "__main__":
	history = HistoryPage(20132110010311)
	html = history.fetchPage()._result
	count = 0
	while (history.matchpage()):
		print history.hisParserHtml(history.fetchPage()._result)
		history.nextpage()
		count=count+1
	print count
