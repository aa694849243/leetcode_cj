# coding=utf-8
'''

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

 

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.s = {}
        self.qu = deque()

    def get(self, key: int) -> int:
        if key in self.s:
            self.qu.remove(key)
            self.qu.append(key)
            return self.s[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.s:
            self.s[key] = value
            self.qu.remove(key)
            self.qu.append(key)
        else:
            if len(self.qu) < self.capacity:
                self.s[key] = value
                self.qu.append(key)
            else:
                a = self.qu.popleft()
                self.s.pop(a)
                self.s[key] = value
                self.qu.append(key)


# 利用collections模块的ordereddict
import collections


class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 利用双向链表实现有序字典

# 定义双向链表
class DLinkedNode:
    def __init__(self, key=0,val=0):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key


# 定义缓存机制
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move2head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.move2head(self.cache[key])
        else:
            if self.size < self.cap:
                node = DLinkedNode(val=value, key=key)
                self.cache[key] = node
                self.addheadnode(node)
                self.size += 1
            else:
                node = DLinkedNode(val=value, key=key)
                rkey = self.removetailhead()
                self.cache.pop(rkey)
                self.cache[key] = node
                self.addheadnode(node)

    def removenode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addheadnode(self, node):
        a = self.head.next
        self.head.next = node
        node.next = a
        node.prev=self.head
        a.prev=node

    def move2head(self, node):
        self.removenode(node)
        self.addheadnode(node)

    def removetailhead(self):
        node = self.tail.prev
        self.removenode(node)
        return node.key


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 1)
cache.put(2,2)
cache.get(2)
cache.put(1, 1)
cache.put(4,1)
cache.get(2)
