# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def beam(n,array):
    x_list = [0 for i in range(n)]
    y_list = [0 for i in range(n)]
    for i in range(n):
        x_list[i] = array[i][0]
        y_list[i] = array[i][1]
    print x_list
    print y_list

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
    RC[i] = map(int ,RC[i])

# エラーチェック
if len(RC) != int(K):
    print "Error: 座標の数とKの値が一致しません"
    sys.exit()

print RC

beam(int(K), RC)
