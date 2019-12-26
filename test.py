#! /usr/bin/env python3
#coding:utf8

from login import login

test = login('你的学号', '你的密码')
test.getHidden()
test.getCheckCode()
test.postData()
test.getTable()
#test.outPut()
test.getClassTable()
