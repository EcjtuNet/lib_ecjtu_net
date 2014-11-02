#!/usr/bin/env python
# -*- coding: utf-8 -*-
#任务计划实现
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler(timezone=utc)
from core.Page.UserPage import UserPage
from core.Page.Request import Request
from core.User import User
from pony.orm import *
import time
import Config

def cronwork1():
    print '-START- fresh users\' borrowed books'
    users = []
    with db_session:
        users = select(u for u in User)[:]
    for u in users:
        if u.renew_flag:
            request = Request().setCookie(u.student_id, u.password)
        with db_session:
            u = User.get(student_id=u.student_id)
            p = UserPage(u.student_id, u.password) 
            books = p.fetchHtml().parseHtml()['books']
            [r.delete() for r in u.readings]
            for b in books:
                name = b[1].decode('utf-8')
                code = b[0]
                borrow_time = b[2]
                due_time = b[3]
                renewed = False if b[4]=='0' else True
                renew_link = b[5]
                index_code = b[6]
                address = b[7].decode('utf-8')
                #AutoRenew
                if u.renew_flag:
                    timestamp = time.mktime(time.strptime(due_time, '%Y-%m-%d'))
                    if timestamp - time.time() < float(Config.get('auto_renew_time')) and renewed==False:
                        request.get(Config.get('lib_base_url')+renew_link)
                        renewed == True
                #SaveData
                u.readings.create(
                        name = name,
                        code = code,
                        borrow_time = borrow_time,
                        due_time = due_time,
                        renewed = renewed,
                        renew_link = renew_link,
                        index_code = index_code,
                        address = address
                        )
    print '-STOP- fresh users\' borrowed books'

def cronwork2():
    pass

sched.add_job(cronwork1, 'interval', hours=5)
sched.add_job(cronwork2, 'interval', hours=12)
def start():
    sched.start()
    print 'cronwork started'
