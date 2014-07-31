#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Request import Request

class Page:
	def fetchHtml(self):
		pass

	def parseHtml(self, html=''):
		return self.parser.parse(html) if html else self.parser.parse(self._html)

	def html(self):
		return self._html

	def nextPage(self):
		self.page += 1

	def page(self, page):
		self.setPage(page)
		self.fetchHtml()

	def setPage(self, page):
		self.page = page