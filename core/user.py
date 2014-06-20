#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
import re
from cookielib import CookieJar

class ReaderInfo():
	def __init__(self, username, password=''):
		self.cookie = self.readerCookie(username, password)
	def getInfo(self):
		opener = urllib2.build_opener(self.cookie)
		request = urllib2.Request(
			url	 = 'http://lib.ecjtu.jx.cn/gdweb/ReaderTable.aspx',
			headers = {'Host' : '172.16.15.229',
				'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
				'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
		f = opener.open(request)
		html = f.read()
		return html
	def parse(self, html):
		info_regs = {
			'ID' : re.compile(r'<span id="LblCarcCode">(\d)</span>'),
			'name' : re.compile(r'<span id="LblreaderName">(.*)</span>'),
			'fk' : re.compile(r'<span id="LblQfk">(.*)</span>'),
			'borrowed' : re.compile(r'<span id="LblBrooyCount">(\d)</span>')}
		print html
		for i in info_regs:
			print info_regs[i].match(html)
	def readerCookie(self, username, password=''):
		cookies = urllib2.HTTPCookieProcessor()
		opener = urllib2.build_opener(cookies)
		login_data = urllib.urlencode({
			'logintype' : 'BARCODE',
			'login.x' : 0,
			'login.y' : 0,
			'fullname' : username,
			'password' : password})
		login_request = urllib2.Request(
			url	 = 'http://lib.ecjtu.jx.cn/gdweb/CheckTick.aspx',
			headers = {'Content-Type' : 'application/x-www-form-urlencoded', 
				'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Host' : '172.16.15.229',
				'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'},
			data	= login_data)
		f = opener.open(login_request)
		return cookies

ReaderInfo('20120310060426').parse(ReaderInfo('20120310060426').getInfo())