#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from core.Page.SearchPage import SearchPage
from core.Page.SearchRule import SearchRule
import json
app = Flask(__name__)
app.debug = True
@app.route("/api/search")
def search():
    key = request.args.get('key').encode('utf8')
    r = SearchRule().add('title', key)
    s = SearchPage(r)
    result = s.fetchHtml().parseHtml()
    return json.dumps(result)
    

@app.route("/")
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
