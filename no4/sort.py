# !/usr/bin/env python
# -*- coding: utf-8 -*-

def main(array):
    old = array
    new = sorted(array)
    m = 0
    n = 0

    # mを求める
    for i in range(len(old)):
        if old[i] != new[i]:
            m = i
            old = old[i:]
            new = new[i:]
            break
    # nを求める
    for j in range(len(old)):
        if old[-j-1] != new[-j-1]:
            n = m + len(old) - j
            break
    print "m="+str(m)
    print "n="+str(n)

# debug
test = [1,2,4,7,10,11,7,12,8,16,18,19]

main(test)
