# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack:

    def __init__(self,stack):
        self.stack = stack
        self.leng = len(self.stack)

    def empty():
        # return "True" if self.leng == 0 else "False"
        if self.leng == 0:
            return "true"
        else:
            return "false"

    def T_peek():
        return self.stack[-1]

    def T_pop():
        s = self.stack[-1]
        self.stack.pop()
        return s

    def T_push(obj):
        self.stack.append(obj)

    def size():
        return leng
