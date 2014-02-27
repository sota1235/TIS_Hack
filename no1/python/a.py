# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack:

    def __init__(self,stack):
        self.stack = stack
        self.leng = len(self.stack)

    def empty(self):
        # return "True" if self.leng == 0 else "False"
        if self.leng == 0:
            return "true"
        else:
            return "false"

    def T_peek(self):
        return self.stack[-1]

    def T_pop(self):
        s = self.stack[-1]
        self.stack.pop()
        return s

    def T_push(self,obj):
        self.stack.append(obj)

    def size(self):
        return leng
