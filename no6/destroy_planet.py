# !/usr/bin/env python
# -*- coding: utf-8 -*-



# input
print "Enter N"
N = raw_input()
print "Enter K"
K = raw_input()
print "Enter (R,C)"
RC = raw_input()

# 座標データ整形
RC = RC.lstrip('{')
RC = RC.rstrip('}')
RC = RC.split('(')
RC.pop(0)
print RC
for i in range(len(RC)):
    RC[i] = RC[i].replace(')', '')
    RC[i] = RC[i].rstrip(',')
    RC[i] = RC[i].split(',')
print RC
