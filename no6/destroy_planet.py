# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def beam(n,k,array):
    # param
    x_list = [0 for i in range(n)]
    y_list = [0 for i in range(n)]
    beam_t = 0
    beam_array = []
    planet_array = array

    # make list of x,y
    for i in range(k):
        x_list[array[i][0]] += 1
        y_list[array[i][1]] += 1
    print x_list
    print y_list

    # 発射する列,行を決定
    while(sum(x_list) != 0 and sum(y_list) != 0):
        flag = 0 # 0:x 1:y
        box = []
        if max(x_list) < max(y_list):
            index = y_list.index(max(y_list))
            y_list[index] = 0
            flag = 1
        else:
            index = x_list.index(max(x_list))
            x_list[index] = 0
            flag = 0
        print index
        print flag
        print planet_array
        for i in range(len(planet_array)):
            print i
            print flag
            print planet_array[i][flag]
            if planet_array[i][flag] == index:
                box.append(planet_array[i])
                planet_array[i] = [n+1, n+1]
        if box != []:
            beam_array.append(box)
            beam_t += 1
    print beam_array
    print beam_t

# input
"""
print "Enter N"
N = raw_input()
print "Enter K"
K = raw_input()
print "Enter (R,C)"
RC = raw_input()
"""

# debug
N = 3
K = 4
RC = "{(0,0),(0,2),(1,1),(2,1)}"

# 座標データ整形
RC = RC.lstrip('{')
RC = RC.rstrip('}')
RC = RC.split('(')
RC.pop(0)
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

beam(int(N),int(K), RC)
