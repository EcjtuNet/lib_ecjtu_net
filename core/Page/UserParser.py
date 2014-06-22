#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Parser import Parser
import re

class UserParser(Parser):
	def __init__(self, html=''):
		if html :
			self.html = html
	def parse(self, html=''):
		html = html if html else self.html
		info = {}
		info_reg = {
			'ID' : r'<span id="LblCarcCode">(\d+)</span>',
			'name' : r'<span id="LblreaderName">(.*)</span>',
			'fk' : r'<span id="LblQfk">(.*)</span>',
			'borrowed' : r'<span id="LblBrooyCount">(\d+)</span>'
		}
		for i in info_reg:
			info[i] = re.findall(info_reg[i], html, re.M)[0]
		borrowed = {}
		borrowed_reg = r'<tr>\s+<td>(\d+)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>\s+(\d+)\s+<a href=\'(.*)\'>\s+续借</a>\s+</td><td>(.*)</td><td>(.*)</td>\s+</tr>'
		borrowed = re.findall(borrowed_reg, html, re.M)
		info['books'] = borrowed
		return info