#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from core.Page.SearchPage import SearchPage
from core.Page.SearchRule import SearchRule
from core.User import User
import json
app = Flask(__name__)
app.debug = True
@app.route("/api/search")
def search():
    key = request.args.get('key')
    author = request.args.get('author')
    key = key.encode('utf8') if key else ''
    author = author.encode('utf8') if author else ''
    page = 1 if not request.args.get('page') else int(request.args.get('page'))
    r = SearchRule().add('title', key).add('author', author)
    result = SearchPage(r).page(page).parseHtml()
    return json.dumps(result)
    
@app.route("/api/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    u = User().login(username, password)
    if u:
        return json.dumps({'result':True,'token':u.token})
    else:
        return json.dumps({'result':False, 'msg':'Username or password is correct', 'token':''})
    
@app.route("/api/register", methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if User().is_exist(username):
        return json.dumps({'result':False, 'msg':'Username exist'})
    u = User().register(username, password)
    if u:
        return json.dumps({
            'result':True,
            'msg':'ok',
            'user':u
        })
    else:
        return json.dumps({'result':False, 'msg':'Register error'})

@app.route("/")
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
