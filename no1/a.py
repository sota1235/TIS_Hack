# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack:

    def __init__(stac):
        self.stac = stac

    def boolean empty():
        return True if len(stac)==0 else return False

    def T_peek():
        return stac(0)

    def T_pop():
        s = stac(0)
        stac.pop(0)
        return s

    def T_push(obj):
        stac.insert(0, obj)

    def size():
        return len(stac)
