# !/usr/bin/env python
# -*- coding: utf-8 -*-

# def minus(a, b):


def multiply(a, b):
    ans = 0
    for i in range(b):
        ans += a
    return ans

# 小数バージョン
def devide(a, b):
    ans = 0
    rest = 0
    while b < a:
        ans += 1
        b += b
    return ans

# debug
print multiply(3, 4)
print devide(15, 3)
