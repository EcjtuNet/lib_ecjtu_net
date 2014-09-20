#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Parser import Parser
import re

class SearchParser(Parser):
	def __init__(self, html=''):
		if html :
			self.html = html
	def parse(self, html=''):
		html = html if html else self.html
		reg = r'<table width="100%" border="0">[\s\S]*'
		reg = r"<a class='WL'.*>(.*)&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.*</a></span></td>[\s\S]*"
		reg += r"<td>索书号：(.*)&nbsp&nbsp&nbsp&nbsp&nbspISBN/ISSN：(.*)&nbsp</td>[\s\S]*"
		reg += r'<span id="Repeater1_ctl01_Label1">(.*)</span>&nbsp&nbsp&nbsp&nbsp[\s\S]*'
		reg += r'<span id="Repeater1_ctl01_Label3">(.*)</span>[\s\S]*'
		reg += r'<span id="Repeater1_ctl01_Lbelinfor">(.*)</span>[\s\S]*'
		reg += r'<span id="Repeater1_ctl01_LblZrz">(.*)</span></span></td>'
		books = re.findall(reg, html, re.M)
		return books
