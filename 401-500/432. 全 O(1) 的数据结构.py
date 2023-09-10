# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
#
#  实现 AllOne 类：
#
#
#  AllOne() 初始化数据结构的对象。
#  inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
#  dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例
# 保证：在减少计数前，key 存在于数据结构中。
#  getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
#  getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
#
#
#  注意：每个函数都应当满足 O(1) 平均时间复杂度。
#
#
#
#  示例：
#
#
# 输入
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# 输出
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# 解释
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "leet"
#
#
#
#
#  提示：
#
#
#  1 <= key.length <= 10
#  key 由小写英文字母组成
#  测试用例保证：在每次调用 dec 时，数据结构中总存在 key
#  最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10⁴ 次
#
#
#  Related Topics 设计 哈希表 链表 双向链表
#  👍 308 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:

    def __init__(self):
        self.head, self.tail = Node(-1), Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.key2cnt = {}
        self.cnt2node = {}

    def inc(self, key: str) -> None:
        if key not in self.key2cnt:
            if 1 not in self.cnt2node:
                self.cnt2node[1] = Node(1)
                self.cnt2node[1].keys.add(key)
                self.key2cnt[key] = 1
                self.addAfter(self.head, self.cnt2node[1])
            else:
                self.cnt2node[1].keys.add(key)
                self.key2cnt[key] = 1
        else:
            cnt = self.key2cnt[key]
            self.key2cnt[key] += 1
            self.cnt2node[cnt].keys.remove(key)
            if cnt + 1 not in self.cnt2node:
                self.cnt2node[cnt + 1] = Node(cnt + 1)
                self.cnt2node[cnt + 1].keys.add(key)
                self.addAfter(self.cnt2node[cnt], self.cnt2node[cnt + 1])
            else:
                self.cnt2node[cnt + 1].keys.add(key)
            if not self.cnt2node[cnt].keys:
                self.remove_node(self.cnt2node[cnt])
                self.cnt2node.pop(cnt)

    def dec(self, key: str) -> None:
        cnt = self.key2cnt[key]
        if cnt == 1:
            self.key2cnt.pop(key)
            self.cnt2node[1].keys.remove(key)
            if not self.cnt2node[1].keys:
                self.remove_node(self.cnt2node[1])
                self.cnt2node.pop(1)
        else:
            self.key2cnt[key] -= 1
            self.cnt2node[cnt].keys.remove(key)
            if cnt - 1 not in self.cnt2node:
                pre_node= self.cnt2node[cnt].prev
                self.cnt2node[cnt - 1] = Node(cnt - 1)
                self.cnt2node[cnt - 1].keys.add(key)
                self.addAfter(pre_node, self.cnt2node[cnt-1])
            else:
                self.cnt2node[cnt - 1].keys.add(key)
            if not self.cnt2node[cnt].keys:
                self.remove_node(self.cnt2node[cnt])
                self.cnt2node.pop(cnt)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""

    def addAfter(self, node, newNode):
        newNode.prev = node
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# leetcode submit region end(Prohibit modification and deletion)
