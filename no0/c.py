# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# b.pyより
def isSubstring(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    count = 0
    # s2の一文字目がなかったら終了
    if not l2[0] in l1:
        sys.exit()
    while(l2[0] in l1):
        index = l1.index(l2[0])
        for i in range(len(l2)):
            if not l1[index+i] == l2[i]:
                break
            if i+1 == len(l2):
                print "true"
                sys.exit()
        l1.pop(index)
    print "false"
    sys.exit()

# デバッグ用
s1_d = sys.argv[1]
s2_d = sys.argv[2]

isSubstring(s1_d+s1_d, s2_d)
