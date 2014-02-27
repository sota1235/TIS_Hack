# !/usr/bin/env python
# -*- coding: utf-8 -*-

def minus(a, b):
    ans = 0
    flag = 'a' if a > b else 'b'
    while a != b:
        ans += 1
        if a > b:
            b += 1
        else:
            a += 1
    return ans if flag == 'a' else -ans

def multiply(a, b):
    ans = 0
    for i in range(b):
        ans += a
    return ans

# 実数バージョン
def devide(a, b):
    ans = 0
    while b < a:
        ans += 1
        b += b
    return ans

# debug
print multiply(3, 4)
print devide(15, 3)
print minus(15, 3)
