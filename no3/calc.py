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
    # 1を下回る場合
    # 返り値がintの場合はルール違反…
    if a < b: return str(a) + "/" + str(b)
    ans = 0
    bb = b
    while b < a:
        ans += 1
        b += bb
    return ans

# decimal number ver
def devide_d(a, b):
    ans = 0
    bb = b
    while b < a:
        ans += 1
        b += bb
    b -= bb
    # 小数第一位
    while b < a:
        ans += 0.1
        b += multiply(0.1, bb)
    return ans

# debug
print "3 * 4 = " + str(multiply(3, 4))
print "15 / 3 = " + str(devide(15, 3))
print "15 - 18 = " + str(minus(15, 18))
print "5 / 2 = " + str(devide_d(5, 2))

# 発表用
while 1:
    print "please operation"
    print "ex) 3 + 7"
    str = list(raw_input())
    if len(str) != 3:
        print "Error: 書式が違います"
        continue
    a = int(str[0]), b = int(str[2])
    calc = str[1]
    if calc == "+":
        ans = a + b
    else if calc == "-":
        ans = minus(a,b)
    else if calc == "*":
        ans = multiply(a,b)
    else if calc == "/":
        ans = devide(a,b)
    else:
        print "Error: 記号が無効です"
        continue
    print "answer : " + ans
