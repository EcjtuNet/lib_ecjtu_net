#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("Parser/")
from Request import Request

class Page:
	def __init__(self):
		pass

	def fetchHtml(self):
		pass

	def parseHtml(self, html=''):
		return self.parser.parse(html) if html else self.parser.parse(self.html)

	def html(self):
		return self.html