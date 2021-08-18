#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存
# 被填满时，它应该删除最近最少使用的项目。
#
#  它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
#  获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新
# 的数据值留出空间。
#
#  示例:
#
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#  Related Topics 设计 哈希表 链表 双向链表
#  👍 110 👎 0

# 双向链表
class DLinkeNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.nxt = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.ca = capacity
        self.h = DLinkeNode()
        self.t = DLinkeNode()
        self.h.nxt = self.t
        self.t.pre = self.h
        self.m = {}
        self.size = 0

    def movetohead(self, node):
        p = node.pre
        n = node.nxt
        p.nxt = n
        n.pre = p
        two = self.h.nxt
        self.h.nxt = node
        node.pre = self.h
        node.nxt = two
        two.pre = node

    def add_head(self, node):
        two = self.h.nxt
        self.h.nxt = node
        node.pre = self.h
        node.nxt = two
        two.pre = node

    def del_tail(self, node):
        self.t.pre = self.t.pre.pre
        self.t.pre.nxt = self.t

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]
            self.movetohead(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.m:
            node = DLinkeNode(key, value)
            self.m[key] = node
            self.add_head(node)
            if self.size < self.ca:
                self.size += 1
            else:
                del_node = self.t.pre
                self.m.pop(del_node.key)
                self.del_tail(node)
        else:
            node = self.m[key]
            node.value = value
            self.movetohead(node)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(10)
a = ["put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get",
     "get", "put", "put", "get", "put", "put", "get"]
b = [[1, 30], [9, 12], [4, 30], [9, 3], [9], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23],
     [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [6]]
for i, ch in enumerate(a):
    if ch == 'put':
        obj.put(*b[i])
    else:
        obj.get(b[i][0])
