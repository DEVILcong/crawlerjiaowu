#! /usr/bin/env python3
#coding:utf8

from login import login

test = login('E31714036', '')
test.getHidden()
test.getCheckCode()
test.postData()
test.getTable()
#test.outPut()
