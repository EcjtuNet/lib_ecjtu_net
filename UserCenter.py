#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2
import json

class UserCenter:
    base_url = 'http://user.ecjtu.net'
    api_url = '/api'
    @classmethod
    def login(cls, username, password):
        r = cls.request('/login', {'username': username, 'password': password})
        if not r:
            return False
        u = User()
        u.token = r['token']
        u.username = username
        return u

    @classmethod
    def showUser(cls, username, token):
        u = cls.request('/user/'+username+'?token='+token)
        if u:
            return u['user']
        return False

    @classmethod
    def editUser(cls, username, token, data):
        data['token'] = token
        u = cls.request('/user/'+username, data)
        if u:
            return json.loads(u['user'])
        return False

    @classmethod
    def request(cls, url, data=False):
        url = cls.base_url + cls.api_url + url
        if data:
            data = urllib.urlencode(data)
        if data:
            r = urllib2.urlopen(url, data)
        else:
            r = urllib2.urlopen(url)
        s = r.read()
        r.close()
        if not s:
            return False
        a = json.loads(s)
        if not a['result']:
            return False
        return a

class User:
    token = ''
    username = ''
    data = False
    
    def __getattr__(self, name):
        if not self.data:
            self.data = UserCenter.showUser(self.username, self.token)
        return self.data[name]

    def __setattr__(self, name, value):
        if name == 'token':
            self.__dict__['token'] = value
        elif name == 'username':
            self.__dict__['username'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        elif name in self.__dict__['data']:
            self.__dict__['data'][name] = value

    def checkToken(self):
        return self.sync()

    def sync(self):
        u = UserCenter.editUser(self.username, self.token, self.data)
        if not u:
            return False
        for i in u:
            self.data[i] = u[i]
            return True

if __name__ == '__main__':
    u = UserCenter.login('20120310060426', '096817')
    print u.token
    print u.username
    print u.Birth
