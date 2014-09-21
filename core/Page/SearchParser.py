#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from Parser import Parser
import re

class SearchParser(Parser):
	def __init__(self, html=''):
		if html :
			self.html = html
	def parse(self, html=''):
		html = html if html else self.html
                html = unicode(BeautifulSoup(html))
                reg = ''
                reg += u'<span id="Repeater1_ctl\d*_LabeBookName"><a .*>(.*)\xa0{8}\[[\s\S]*?'
                reg += u'<td>索书号：(.*)\xa0{4}&amp;nbspISBN;/ISSN：(.*)\xa0</td>[\s\S]*?'
                reg += u'<span id="Repeater1_ctl\d*_Label1">(.*)</span>\xa0{4}\s*'
                reg += u'<span id="Repeater1_ctl\d*_Label3">(.*)</span>[\s\S]*?'
                reg += u'<span id="Repeater1_ctl\d*_Lbelinfor">(.*)</span>[\s\S]*?'
                reg += u'<span id="Repeater1_ctl\d*_LblZrz">(.*)</span></span></td>[\S\s]*?'
                reg += u'馆藏数:\[(\d*)\].*可外借数:\[(\d*)\]'
		books = re.findall(reg, html, re.M) 
		return books                
