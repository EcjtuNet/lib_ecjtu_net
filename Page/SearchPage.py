#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cookielib
import urllib2
from Page import Page
from SearchParser import SearchParser
from SearchRule import SearchRule
from Request import Request
import re
import math
import sys
sys.path.append('../')
import Cache

class SearchPage(Page):
    def __init__(self, rule):
        self.parser = SearchParser()
        self.rule = rule
        self._page = 1
        self.BASE_URL = 'http://172.16.15.229'
        self._per_page = 5
        self.total_count = 0
        self._html = ''

    def fetch(self):
        post_url = self.BASE_URL + '/gdweb/CombinationScarch.aspx'
        get_url = self.BASE_URL + '/gdweb/ScarchList.aspx?page='+str(self._page)
        data = self.rule.make()
        html = Cache.get(get_url + ':' + data)
        if not html: 
            r = Request()
            r.post(post_url, data)
            html = r.get(get_url)
            Cache.set(get_url + ':' + data, html)
        self._html = html
        return self 

    def set_total_count(self):
        if self.total_count == 0:
            reg = u'width:100%;">...(\d*)'
            if not self._html:
                self.fetch()
            total_page = int(re.findall(reg, self._html, re.M)[0])
            s = SearchPage(self.rule)
            s.total_count=1
            self.total_count = (total_page-1)*self._per_page + len(s.fetch().parse())

    def offset(self, offset, limit):
        self.set_total_count()
        if (offset-1)*limit > self.total_count:
            return False
        output = []
        begin = (offset-1)*limit + 1
        begin_page = int(math.ceil(begin/float(self._per_page)))
        begin_offset = (begin-1)%self._per_page
        end = begin + limit - 1
        end_page = int(math.ceil(end/float(self._per_page)))
        end_offset = (end-1)%self._per_page
        for i in range(begin_page, end_page+1):
            s = SearchPage(self.rule)
            s._page = i
            if limit < 5 and begin_page==end_page:
                output += s.fetch().parse()[begin_offset:begin_offset+limit]
            elif i == begin_page:
                output += s.fetch().parse()[begin_offset:self._per_page+1]
            elif i == end_page:
                output += s.fetch().parse()[0:end_offset+1]
            else:
                output += s.fetch().parse()
        if __name__ == "__main__":
            print begin,begin_page,begin_offset,end,end_page,end_offset
        return output


if __name__ == "__main__":
    rule = SearchRule().add('title', 'ruby')
    s = SearchPage(rule)
    print s.offset(4,1)


