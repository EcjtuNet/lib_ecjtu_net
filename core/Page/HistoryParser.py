#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Parser import Parser
import re

class HistoryParser(Parser):
	def __init__(self, html=''):
		if html :
			self.html = html

	def parse(self,html=''):
		html = html if html else self.html
		reg = r'<td>(.*)</td><td>([0-9]*)</td><td>[0-9]*</td><td>(.*)</td><td>(.*)</td>'
		return re.findall(reg, html, re.M)