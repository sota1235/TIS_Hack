# !/usr/bin/env python
# -*- coding: utf-8 -*-

def minus(a, b):
    ans = 0
    flag = 'a' if a > b else 'b'
    while a != b:
        ans += 1
        if a > b: b += 1
        else: a += 1
    return ans if flag == 'a' else int('-'+str(ans))

def multiply(a, b):
    ans = 0
    for i in range(b): ans += a
    return ans

# integral number ver
def devide(a, b):
    ans = 0
    while b < a:
        ans += 1
        b += b
    return ans

# debug
print "3 * 4 = " + str(multiply(3, 4))
print "15 / 3 = " + str(devide(15, 3))
print "15 - 18 = " + str(minus(15, 18))
