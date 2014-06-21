#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2,urllib
from cookielib import CookieJar

class Request:
	def __init__(self):
		self.username = username
		self.password = password
	def setCookie(self, username, password=''):
		cookies = urllib2.HTTPCookieProcessor()
		opener = urllib2.build_opener(cookies)
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

	def get(self, url):
		return self.sendRequest()

	def post(self, url, data):
		return self.sendRequest(data)

	def sendRequest(self, data=''):
		request = (
			url = url,
			headers = {'Content-Type' : 'application/x-www-form-urlencoded', 
				'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Host' : '172.16.15.229',
				'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
		if data:
			request['data'] = data
		request = urllib2.Request(request)
		opener = self.cookie ? urllib2.build_opener(self.cookie) : urllib2.build_opener()
		f = opener.open(request)
		return f.read()