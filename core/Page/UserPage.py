#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page import Page
from UserParser import UserParser
from Request import Request

class UserPage(Page):
	def __init__(self, username, password=''):
		self.parser = UserParser()
		self.username = username
		self.password = password

	def fetchHtml(self):
		self._html = Request().setCookie(self.username, self.password).get('http://lib.ecjtu.jx.cn/gdweb/ReaderTable.aspx')
		return self

if __name__ == "__main__":
	userpage = UserPage(20120310060426)
	print userpage.fetchHtml().html()
	print userpage.parseHtml()