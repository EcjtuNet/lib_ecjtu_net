#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2,urllib
from cookielib import CookieJar

class Request:
	def __init__(self):
		pass

	def setCookie(self, username, password=''):
		self.username = username
		self.password = password
		cookie = urllib2.HTTPCookieProcessor()
		opener = urllib2.build_opener(cookie)
		login_data = urllib.urlencode({
			'logintype' : 'BARCODE',
			'login.x' : 0,
			'login.y' : 0,
			'fullname' : self.username,
			'password' : self.password})
		login_request = urllib2.Request(
			url	 = 'http://lib.ecjtu.jx.cn/gdweb/CheckTick.aspx',
			headers = {'Content-Type' : 'application/x-www-form-urlencoded',
				'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Host' : '172.16.15.229',
				'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'},
			data	= login_data)		
		f = opener.open(login_request)
		self.cookie = cookie
		return self

	def get(self, url):
		return self.sendRequest(url)

	def post(self, url, data):
		return self.sendRequest(url, data)

	def sendRequest(self, url, data=''):
		headers = {'Content-Type' : 'application/x-www-form-urlencoded', 
			'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Host' : '172.16.15.229',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
		if data :
			request = urllib2.Request(url=url, headers=headers, data=data)
		else :
			request = urllib2.Request(url=url, headers=headers)
		opener = urllib2.build_opener(self.cookie) if hasattr(self, 'cookie') else urllib2.build_opener()
		f = opener.open(request)
		return f.read()