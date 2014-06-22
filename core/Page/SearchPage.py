#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Page import Page
from SearchParser import SearchParser
from SearchRule import SearchRule

class SearchPage(Page):
	def __init__(self, rule):
		self.parser = SearchParser()
		self.rule = rule
		self.page = 1

	def fetchHtml(self):
		url = 'http://lib.ecjtu.jx.cn/gdweb/ScarchList.aspx?Page=' + str(self.page)
		data = self.rule.make()
		self.html = Request().post(url, data)
		return self

	def nextPage(self):
		self.page += 1

	def page(self, page):
		self.setPage(page)
		self.fetchHtml()

	def setPage(self, page):
		self.page = page


if __name__ == "__main__":
	rule = SearchRule().add('title', 'python')
	searchpage = SearchPage(rule)
	print searchpage.fetchHtml().html()
	print searchpage.parseHtml()