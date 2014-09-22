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
    key = request.args.get('key')
    author = request.args.get('author')
    key = key.encode('utf8') if key else ''
    author = author.encode('utf8') if author else ''
    page = 1 if not request.args.get('page') else int(request.args.get('page'))
    r = SearchRule().add('title', key).add('author', author)
    result = SearchPage(r).page(page).parseHtml()
    return json.dumps(result)
    

@app.route("/")
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
