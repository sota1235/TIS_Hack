# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def isSubstring(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    # 文字数が違う場合
    if len(s1) != len(s2):
        print "false"
        sys.exit()

    while(len(s1) != 0):
        if s1[0] in s2:
            index = s2.index(s1[0])
        else:
            print "false"
            sys.exit()
        i = 0
        while(s1[0] == s2[index] and len(s1) != 1):
            s1.pop(0)
            s2.pop(index)
            if index == len(s2):
                break
        if len(s1) == 1:
            if s1[0] == s2[0]:
                print "true"
            else:
                print "false"
            sys.exit()

s1_d = sys.argv[1]
s2_d = sys.argv[2]

isSubstring(s1_d, s2_d)
