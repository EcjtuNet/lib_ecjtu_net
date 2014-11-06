#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from core.Page.SearchPage import SearchPage
from core.Page.SearchRule import SearchRule
from core.Model import *
from pony.orm import *
from pony.orm.serialization import to_dict
import json
import cronwork

app = Flask(__name__)

if Config.get('develop'):
    app.debug = True

@app.route("/api/search")
def search():
    key = request.args.get('key')
    author = request.args.get('author')
    key = key.encode('utf8') if key else ''
    author = author.encode('utf8') if author else ''
    page = 1 if not request.args.get('page') else int(request.args.get('page'))
    limit = 20 if not request.args.get('limit') else int(request.args.get('limit'))
    r = SearchRule().add('title', key).add('author', author)
    result = SearchPage(r).offset(page, limit)
    return json.dumps(result)
    
@app.route("/api/login", methods=['POST'])
@db_session
def login():
    username = request.form['username']
    password = request.form['password']
    u = User.login(username, password)
    if u:
        return json.dumps({'result':True,'token':u.token.to_dict()['token']})
    else:
        return json.dumps({'result':False, 'msg':'Username or password is incorrect', 'token':''})
    
@app.route("/api/register", methods=['POST'])
@db_session
def register():
    username = request.form['username']
    password = request.form['password']
    if User.is_exist(username):
        return json.dumps({'result':False, 'msg':'Username exist'})
    u = User.register(username, password)
    if u:
        return json.dumps({
            'result':True,
            'msg':'ok',
            'user':u.to_dict()
            })
    else:
        return json.dumps({'result':False, 'msg':'Register error'})

@app.route("/api/user/<int:student_id>/history")
@db_session
def history(student_id):
    u = User.getBySid(str(student_id))
    h = to_dict(u.histories)
    return json.dumps({
        'result':True, 
        'user':u.to_dict(exclude='password'), 
        'history':h
        })

@app.route("/api/user/<int:student_id>/borrowed")
@db_session
def borrowed(student_id):
    u = User.getBySid(str(student_id))
    r = to_dict(u.readings)['Reading']
    r = [r[b] for b in r]
    result = []
    for row in r:
        del row['user']
        result.append(row)
    return json.dumps({
        'result':True,
        'user':u.to_dict(exclude='password'),
        'readings':result
        })

@app.route("/api/user/<int:student_id>")
@db_session
def user(student_id):
    u = User.getBySid(str(student_id))
    if not u :
        return json.dumps({'result':False, 'msg':'No such user'})
    return json.dumps({'result':True, 'user':u.to_dict(exclude='password')}) 

@app.route("/")
def index():
    return 'hello world'

if __name__ == '__main__':
    cronwork.start()
    if Config.get('develop'):
        app.run(host='0.0.0.0', use_reloader=False)
    else:
        app.run(host='0.0.0.0', use_reloader=False)
