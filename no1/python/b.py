# !/usr/bin/env python
# -*- coding: utf-8 -*-

from a import Stack

class Queue:

    def __init__(self,stack):
        self.stack1 = Stack(stack)
        self.stack2 = Stack(stack)
        while !self.stack1.empty(): self.stack1.T_pop()
        while !self.stack2.empty(): self.stack1.T_push(self.stack2.T_pop())

    def add(self,obj):
        stac1.queue.append(obj)

    def T_peek(self):
        return self.stack1.T_peek()

    def T_remove(self):
        self.stack1.T_remove

    def size(self):
        self.stack1.size()
