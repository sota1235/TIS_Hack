# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])
num = n * 2 - 1
q = 1

# 組み合わせの総数
for i in range(num):
    if (i+1) % 2 == 1:
        q *= i+1

# 挿入位置の組み合わせの配列
p = [[0 for i in range(n)] for j in range(q)]

