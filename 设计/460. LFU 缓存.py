'''请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：

LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
void put(int key, int value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。
注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

 

进阶：

你是否可以在 O(1) 时间复杂度内执行两项操作？
 

示例：

输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);
lFUCache.put(2, 2);
lFUCache.get(1);      // 返回 1
lFUCache.put(3, 3);   // 去除键 2
lFUCache.get(2);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
lFUCache.put(4, 4);   // 去除键 1
lFUCache.get(1);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
lFUCache.get(4);      // 返回 4
 

提示：

0 <= capacity, key, value <= 104
最多调用 105 次 get 和 put 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self, key, val, pre=None, nxt=None, freq=0):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt
        self.freq = freq

    def insert(self, node):
        node.pre = self
        node.nxt = self.nxt
        self.nxt.pre = node
        self.nxt = node


def creat_link():  # 自定义freq链表类型
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nxt = tail
    tail.pre = head
    return (head, tail)


import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.keymap = {}  # 存储key-Node对
        self.freqmap = collections.defaultdict(creat_link)
        self.size = 0
        self.minfreq = 0
        self.capacity = capacity

    def delnode(self, node):
        link = self.freqmap[node.freq]
        nxtnode = node.nxt
        prenode = node.pre
        prenode.nxt = nxtnode
        nxtnode.pre = prenode
        if link[0].nxt == link[1]:
            self.freqmap.pop(node.freq)

    def increase(self, node):
        self.delnode(node)
        if node.freq not in self.freqmap and node.freq == self.minfreq:
            self.minfreq += 1
        node.freq += 1
        self.freqmap[node.freq][1].pre.insert(node)

    def get(self, key: int) -> int:
        if key in self.keymap:
            node = self.keymap[key]
            self.increase(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keymap:
                node = self.keymap[key]
                self.increase(node)
                node.val = value
            else:
                if self.size < self.capacity:
                    self.size += 1
                else:
                    node = self.freqmap[self.minfreq][0].nxt
                    self.delnode(node)
                    self.keymap.pop(node.key)
                node = Node(key, value, freq=1)
                if 1 in self.freqmap:
                    self.freqmap[1][1].pre.insert(node)
                else:
                    self.freqmap[1][1].pre.insert(node)
                    self.minfreq = 1
                self.keymap[key]=node
obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.get(3)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)
