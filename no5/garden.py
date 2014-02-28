# !/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import math

def make_shower(n,xyr):
    # xが小さい順にsort
    xyr.sort()
    half = int(math.floor(len(xyr)/2))

    xyr1 = xyr[:half]
    xyr2 = xyr[half:]
    # 新しい円の要件を入れる配列
    if len(xyr1) != 1:
        new_xyr1 = get_newxyr(xyr1)
    else:
        new_xyr1 = xyr1
    if len(xyr2) != 1:
        new_xyr2 = get_newxyr(xyr2)
    else:
        new_xyr2 = xyr2

    # 生成
    while 1:
        if len(new_xyr1) == 1:
            break
        new_xyr1 = get_newxyr(new_xyr1)
    while get_newxyr(new_xyr2):
        new_xyr2 = get_newxyr(new_xyr2)

    print new_xyr1
    print new_xyr2

"""
2つ円を囲む最小の円のxyrを作り
それが1になるまで繰り返す
"""

def get_length(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_newxyr(xyr):
    res = []
    for i in range(0,len(xyr)-1,2):
        x = (xyr[i][0] + xyr[i+1][0]) / 2
        y = (xyr[i][1] + xyr[i+1][1]) / 2
        r = get_length(xyr[i][0],xyr[i][1],xyr[i+1][0],xyr[i+1][0])
        box = [x,y,r]
        res.append(box)
    return res

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
