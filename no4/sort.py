# !/usr/bin/env python
# -*- coding: utf-8 -*-

def main(array):
    old = array
    new = array.sort()
    m = 0
    n = 0

    # mを求める
    for i in range(len(old)):
        if old[i] != new[i]:
            m = i
            old = old[:i+1]
            new = new[:i+1]
            break
    # nを求める
    for j in range(len(old)):
        if old[-i+1] != new[-i+1]:
            n = m + len(old) - i
            break
    print "m="+m
    print "n="+n

# debug
test = [1,2,4,7,10,11,7,12,8,16,18,19]

main(test)
