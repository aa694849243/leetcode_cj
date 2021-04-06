'''请你实现一个数据结构支持以下操作：

Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否则使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串"" 。
GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。
 

挑战：

你能够以 O(1) 的时间复杂度实现所有操作吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-oone-data-structure
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


# 1投机法-不符合O(1)要求  max用法
import collections


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(int)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.lookup[key] += 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.lookup:
            if self.lookup[key] == 1:
                self.lookup.pop(key)
            else:
                self.lookup[key] -= 1

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return max(self.lookup.items(), key=lambda x: x[1], default=[''])[0]

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return min(self.lookup.items(), key=lambda x: x[1], default=[''])[0]


# 2双向链表 O(1)复杂度求最大最小值
import collections


class Node:
    def __init__(self, cnt):
        self.cnt = cnt
        self.keylist = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.keymap = {}
        self.nodenums = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keymap:
            node = self.nodenums[self.keymap[key]]
            if node.cnt + 1 in self.nodenums:
                self.keyoffset(key, 1)
            else:
                self.keymap[key] += 1
                self.insertnode(node, node.cnt + 1)
                self.rmvnodekey(node, key)
                newnode = node.next
                self.nodenums[newnode.cnt] = newnode
                newnode.keylist.add(key)
        else:
            if 1 not in self.nodenums:
                self.insertnode(self.head, 1)
                newnode = self.head.next
                self.nodenums[1] = newnode
                newnode.keylist.add(key)
            else:
                node = self.nodenums[1]
                node.keylist.add(key)
            self.keymap[key] = 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keymap:
            node = self.nodenums[self.keymap[key]]
            if node.cnt > 1:
                if node.cnt - 1 in self.nodenums:
                    self.keyoffset(key, -1)
                else:
                    self.keymap[key] -= 1
                    self.insertnode(node.prev, node.cnt - 1)
                    self.rmvnodekey(node, key)
                    newnode = node.prev
                    self.nodenums[newnode.cnt] = newnode
                    newnode.keylist.add(key)

            else:
                self.rmvnodekey(node, key)
                self.keymap.pop(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return '' if self.head.next == self.tail else next(iter(self.tail.prev.keylist))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return '' if self.head.next == self.tail else next(iter(self.head.next.keylist))

    def keyoffset(self, key, offset):
        nodenum = self.keymap[key]
        node = self.nodenums[nodenum]
        self.keymap[key] += offset
        self.rmvnodekey(node, key)
        newnode = self.nodenums[nodenum + offset]
        newnode.keylist.add(key)

    def insertnode(self, node, val):
        newnode = Node(val)
        a = node.next
        node.next = newnode
        newnode.next = a
        newnode.prev = node
        a.prev = newnode

    def rmvnode(self, node):
        pre = node.prev
        ne = node.next
        pre.next = ne
        ne.prev = pre

    def rmvnodekey(self, node, key):
        node.keylist.discard(key)
        if len(node.keylist) == 0:
            self.nodenums.pop(node.cnt)
            self.rmvnode(node)


# a= ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
# b= [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.inc('b')
obj.inc('c')
obj.inc('c')
obj.inc('c')
obj.dec('b')
obj.dec('b')
obj.getMaxKey()
obj.getMinKey()
obj.dec('a')
obj.getMaxKey()
obj.getMinKey()
