# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

argv = list(sys.argv[1])
count = 0

for s in argv:
    for i in range(len(argv)):
        if s == argv[i]:
            count += 1
    if count > 1:
        print "false"
        sys.exit()
    count = 0

print "true"
