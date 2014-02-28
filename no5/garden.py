# !/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

# input
"""
print "N ="
N = int(raw_input())
print "(X, Y, R) = "
XYR = raw_input()
"""
# debug
XYR = "{(20,10,2),(20,20,2),(40,10,3)}"

# 整形
XYR = XYR[2:-1].split('(')
for i in range(len(XYR)):
    XYR[i] = map(int, XYR[i][0:7].split(','))

print XYR
