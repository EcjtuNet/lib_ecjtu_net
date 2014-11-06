#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Request import Request

class Page:
    def fetch(self):
        pass

    def parse(self, html=''):
        return self.parser.parse(html) if html else self.parser.parse(self._html)

    def html(self):
        return self._html

    def next_page(self):
        self._page += 1
        return self
