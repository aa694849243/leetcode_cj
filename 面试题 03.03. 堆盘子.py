#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行
# 为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与
# 普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行p
# op操作。
#
#  当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1.
#
#  示例1:
#
#   输入：
# ["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
# [[1], [1], [2], [1], [], []]
#  输出：
# [null, null, null, 2, 1, -1]
#
#
#  示例2:
#
#   输入：
# ["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
# [[2], [1], [2], [3], [0], [0], [0]]
#  输出：
# [null, null, null, null, 2, 1, 3]
#
#  Related Topics 栈 设计 链表
#  👍 22 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.l = [[]]

    def push(self, val: int) -> None:
        if len(self.l[-1]) < self.cap:
            self.l[-1].append(val)
        else:
            self.l.append([val])

    def pop(self) -> int:
        if not self.l or not self.l[0]:
            return -1
        a = self.l[-1].pop()
        if not self.l[-1]:
            self.l.pop()
        if not self.l:
            self.l.append([])
        return a

    def popAt(self, index: int) -> int:
        if index >= len(self.l):
            return -1
        if not self.l[index]:
            return -1
        a = self.l[index].pop()
        if not self.l[index]:
            del self.l[index]
        if not self.l:
            self.l.append([])
        return a
