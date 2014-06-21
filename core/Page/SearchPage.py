#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page import Page
from SearchParser import SearchParser
from SearchRule import SearchRule

class SearchPage:
	def __init__(self, rule):
		self.rule = rule
		self.page = 1

	def fetchHtml(self):
		url = 'http://lib.ecjtu.jx.cn/gdweb/ScarchList.aspx?Page=' + str(self.page)
		data = self.rule.make()
		return Request().post(url, data)

	def parseHtml(self, html):
		return SearchParser().parse(html)

	def nextPage(self):
		self.page += 1

	def page(self, page):
		self.setPage(page)
		self.fetchHtml()

	def setPage(self, page):
		self.page = page