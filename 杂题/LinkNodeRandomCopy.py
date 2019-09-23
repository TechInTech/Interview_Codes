# -*- coding:utf-8 -*-

class LinkNodeRandom:
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class CreateLink:
    def __init__(self, lyst):
        self.lyst = lyst
        self.length = len(lyst)

    def get_Link(self):
        p = link = LinkNode()
        i = 0
        while i < self.length:
            node = LinkNode(self.lyst[i])
            p.next = node
            p = p.next
            i += 1
        return link.next
