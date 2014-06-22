#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Parser import Parser
import re

class SearchParser:
	def __init__(self, html=''):
		if html :
			self.html = html
	def parse(self, html=''):
		html = html if html else self.html
		reg = r'<table width="100%" border="0">[\s\S]*'
		reg += r"<a class='WL'.*>(.*)&nbsp[\s\S]*"
		reg += r"索书号：(.*)&nbsp.*ISBN/ISSN：(.*)&nbsp[\s\S]*"
		reg += r'<span id="Repeater1_ctl01_Label1">(.*)</span>[\s\S]*'
		reg += r'<span id="Repeater1_ctl01_Label3">(.*)</span>[\s\S]*'
		reg += r'<span id="Repeater1_ctl01_Lbelinfor">(.*)</span>[\s\S]*'
		reg += r'<span id="Repeater1_ctl01_LblZrz">(.*)</span>[\s\S]*'
		books = re.findall(reg, html, re.M)
		return books