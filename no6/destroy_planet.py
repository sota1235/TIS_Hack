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
        for i in range(len(planet_array)):
            if planet_array[i][flag] == index:
                box.append(planet_array[i])
                planet_array[i] = [n+1, n+1]
        if box != []:
            beam_t += 1
            s = ""
            for i in box:
                s += "(" + str(i[0]) + "," + str(i[1]) + ")と"
            s = s.rstrip("と")
            print str(beam_t) + "発目で" + s + "を破壊"
    print "必要なビーム発射回数: " + str(beam_t)

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
RC = RC[2:-1].split('(')
for i in range(len(RC)):
    RC[i] = map(int, RC[i][0:3].split(','))

# エラーチェック
if len(RC) != int(K):
    print "Error: 座標の数とKの値が一致しません"
    sys.exit()

beam(int(N),int(K), RC)
