#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Parser import Parser
from bs4 import BeautifulSoup

class HistoryParser():
	def __init__(self, html=''):
		if html :
			self.html = html

	def hisParseHtml(self,html=''):
		html = html if html else self.html
		soup = BeautifulSoup(html)
		tag = soup.find_all("tr",style="color:#000066;")
		return tag
