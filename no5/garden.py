# !/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import math

def make_shower(n,xyr):
    # xが小さい順にsort
    xyr.sort()
    half = math.floor(len(xyr)/2)
    xyr1 = xyr[:int(half)]
    xyr2 = xyr[int(half):]
    print xyr1
    print xyr2

# input
"""
print "N ="
N = int(raw_input())
print "(X, Y, R) = "
XYR = raw_input()
"""
# debug
XYR = "{(20,10,2),(10,20,2),(40,10,3)}"

# 整形
XYR = XYR[2:-1].split('(')
for i in range(len(XYR)):
    XYR[i] = map(int, XYR[i][0:7].split(','))

make_shower(3,XYR)
