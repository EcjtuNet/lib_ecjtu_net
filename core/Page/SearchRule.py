#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
#简单实现了组合查询，需修改

class SearchRule:
    def __init__(self):
        self.rule = {
            'ImageButton1.x' : '9',
            'ImageButton1.y' : '10',
            'hidtext1' : '题名',
            'ScriptManager1':'UpdatePanel1|ImageButton1',
            'DropScarchKay1':'馆藏书目库',
            'ImageButton1.x' : '9',
            'ImageButton1.y' : '10',
            'Drop1':'中间一致',
            'DropTJ1':'并且',
            'DropScarchKay2':'检索责任者库',
            'txtKay2':'',
            'Drop2':'中间一致',
            'DropTJ2':'并且',
            'DropScarchKay3':'馆藏典藏库',
            'txtKay3':'',
            'Drop3':'中间一致',
            'DropDB':'1',
            'DropSort':'入藏日期',
            'RadioButtonList1':'正序',
            'hidValue1':'馆藏书目库',
            'hidtext2':'责任者',
            'hidValue2':'检索责任者库',
            'hidtext3':'馆藏地址',
            'hidValue3':'馆藏典藏库',
            '__EVENTVALIDATION' : '/wEWSALzzryLBQLgnZ70BALSwtXkAgLSwsGJCgLK0f+6DwLqzM/lDAL816qKAQKbh4jwBgLK0f+6DwKqvOiVCgLK0f+6DwLK0f+6DwKO2oDNCwLA456VCgKd4ezEDwK9uNjCBAL8rNjCBAKtgdjUAgKSsMX9DgLy2ImNCwLK0cu6DwLqzPvlDAL8156KAQKbh7zwBgLK0cu6DwKqvNyVCgLK0cu6DwLK0cu6DwKO2rTNCwLvp8XVCwKe4ezEDwK+uNjCBAL/rNjCBAKugdjUAgLj/KO8DwKDlO/MCgLK0ce6DwLqzPflDAL815KKAQKbh7DwBgLK0ce6DwKqvNCVCgLK0ce6DwLK0ce6DwKO2rjNCwKKkePqBQKf4ezEDwK/uNjCBAL+rNjCBAKvgdjUAgLlhPOaBwLq69n0CwLr69n0CwLo69n0CwLp69n0CwLu69n0CwLs69n0CwL969n0CwKqkLzdBgLeh9P7CgKI9+rkDgKBkZCRCALKzY3JDQKU3I3JDQL3jKLTDQLSwpnTCALB3/SfBgL8ueK8CALB37iODAL/ueK8CALB38zpBAL+ueK8CE2EJZeTnX7A31iHVD2K4bitc9IC',
            '__VIEWSTATE': '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'
        }
        self.ruleTable = {
            'title' : 'txtKay1',
            'author' : 'txtKay2',
            'address' : 'txtKay3'
        }
    def add(self, key, value):
        if key in self.ruleTable:
            self.rule[self.ruleTable[key]] = value
        return self
    def make(self):
        return urllib.urlencode(self.rule)
