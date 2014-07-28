#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cookielib
import urllib2
from Page import Page
from SearchParser import SearchParser
from SearchRule import SearchRule
from Request import Request

class SearchPage(Page):
	def __init__(self, rule):
		self.parser = SearchParser()
		self.rule = rule
		self.page = 1
		self.BASE_URL = 'http://172.16.15.229'

	def fetchHtml(self):
		post_url = self.BASE_URL + '/gdweb/CombinationScarch.aspx'
		get_url = self.BASE_URL + '/gdweb/ScarchList.aspx?page='+str(self.page)
		data = self.rule.make()
		r = Request()
		self._html = r.post(post_url,data)
		self._result = r.get(get_url)
		print self._result
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
	print searchpage.fetchHtml()._html
	print searchpage.parseHtml()
