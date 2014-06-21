#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page import Page
from UserParser import UserParser

class UserPage(Page):
	def __init__(self, username, password=''):
		self.username = username
		self.password = password

	def fetchHtml(self):
		return Request().setCookie(self.username, self.password).get('http://lib.ecjtu.jx.cn/gdweb/ReaderTable.aspx')

	def parseHtml(self, html):
		return UserParser().parse(html)