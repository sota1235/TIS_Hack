# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])
num = n * 2 - 1
q = 1 # 組み合わせ数
array = []
array_back = []

# 組み合わせの総数
for i in range(num):
    if (i+1) % 2 == 1:
        q *= i+1
        array.append(i+1)
        array_back.append(i+1)

# 挿入位置の組み合わせの配列
p = [[0 for i in range(n)] for j in range(q)]

# 括弧生成用配列の作成
for i in range(q):
    for j in range(n):
        p[i][j] = array[j]
        # 配列の数字を1下げる。0の場合は一周
        if array[j] == 0:
            array[j] = array_back[j]
        else:
            array[j] -= 1

print p
