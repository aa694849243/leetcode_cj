# -*- coding: utf-8 -*-


# 不使用任何库函数，设计一个跳表。
#
#  跳表是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想
# 与链表相似。
#
#  例如，一个跳表包含 [30, 40, 50, 60, 70, 90]，然后增加 80、45 到跳表中，以下图的方式操作：
#
#
# Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons
#
#  跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(
# n))，空间复杂度是 O(n)。
#
#  在本题中，你的设计应该要包含这些函数：
#
#
#  bool search(int target) : 返回target是否存在于跳表中。
#  void add(int num): 插入一个元素到跳表。
#  bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
#
#
#
#  了解更多 : https://en.wikipedia.org/wiki/Skip_list
#
#  注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。
#
#  样例:
#
#  Skiplist skiplist = new Skiplist();
#
# skiplist.add(1);
# skiplist.add(2);
# skiplist.add(3);
# skiplist.search(0);   // 返回 false
# skiplist.add(4);
# skiplist.search(1);   // 返回 true
# skiplist.erase(0);    // 返回 false，0 不在跳表中
# skiplist.erase(1);    // 返回 true
# skiplist.search(1);   // 返回 false，1 已被擦除
#
#
#  约束条件:
#
#
#  0 <= num, target <= 20000
#  最多调用 50000 次 search, add, 以及 erase操作。
#
#  Related Topics 设计
#  👍 69 👎 0

# https://leetcode-cn.com/problems/design-skiplist/solution/1206-she-ji-tiao-biao-pythonshi-xian-by-tuotuoli/
import math
import random

maxlevel = 16
maxrand = 2 ** 16 - 1
power = 2
# 对数随机分布
Randlevel = lambda: maxlevel - int(math.log(random.randint(1, maxrand), power))


class SkipNode:
    def __init__(self, val):
        self.val = val
        self.down = None
        self.right = None


class Skiplist:

    def __init__(self):
        self.left = [SkipNode(float('-inf')) for _ in range(maxlevel)]  # 左右墙壁
        self.right = [SkipNode(float('inf')) for _ in range(maxlevel)]
        for i in range(maxlevel - 1):
            self.left[i].right = self.right[i]
            self.left[i].down = self.left[i + 1]
            self.right[i].down = self.right[i + 1]
        self.left[-1].right = self.right[-1]  # 最后一层只有向右指针没有向下指针
        self.head = self.left[0]

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            if node.right.val < target:
                node = node.right
            elif node.right.val > target:
                node = node.down
            else:
                return True
        return False

    def add(self, num: int) -> None:
        prev = []
        node = self.head
        while node:
            if node.right.val < num:
                node = node.right
            elif node.right.val >= num:
                prev.append(node)  # 将全部的前继节点加入列表
                node = node.down
        arr = [SkipNode(num) for _ in range(Randlevel())]
        t = SkipNode(-1)
        for pre, node in zip(prev[maxlevel - len(arr):], arr):
            node.right = pre.right
            pre.right = node
            t.down = node
            t = node

    def erase(self, num: int) -> bool:
        node = self.head
        ans = False
        while node:
            if node.right.val < num:
                node = node.right
            elif node.right.val > num:
                node = node.down
            else:
                ans = True
                node.right = node.right.right
                node = node.down
        return ans
# Your Skiplist object will be instantiated and called as such:
obj = Skiplist()
obj.add(1)
obj.add(2)
obj.add(3)
obj.search(0)
# param_3 = obj.erase(num)
# leetcode submit region end(Prohibit modification and deletion)
