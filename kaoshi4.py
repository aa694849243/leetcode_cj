#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def func(root):
    lst = []

    def rec(node):
        if not node:
            return
        rec(node.left)
        lst.append(node.val)
        rec(node.right)

    def rec2(li):
        if not li:
            return None
        if len(li) == 1:
            return Node(li[0])
        l, r = 0, len(li)
        mid = l + r >> 1
        node = Node(li[mid])
        lnode = rec2(li[:mid])
        rnode = rec2(li[mid + 1:r])
        node.left = lnode
        node.right = rnode
        return node

    rec(root)
    return rec2(lst)


