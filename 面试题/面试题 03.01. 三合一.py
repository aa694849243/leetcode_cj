#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 三合一。描述如何只用一个数组来实现三个栈。
#
#  你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。s
# tackNum表示栈下标，value表示压入的值。
#
#  构造函数会传入一个stackSize参数，代表每个栈的大小。
#
#  示例1:
#
#   输入：
# ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
# [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
#  输出：
# [null, null, null, 1, -1, -1, true]
# 说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
#
#
#  示例2:
#
#   输入：
# ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
# [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
#  输出：
# [null, null, null, null, 2, 1, -1, -1]
#
#  Related Topics 栈 设计 数组
#  👍 35 👎 0


class TripleInOne:

    def __init__(self, stackSize: int):
        self.limit = stackSize
        self.stacks = [[], [], []]

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stacks[stackNum]) < self.limit:
            self.stacks[stackNum].append(value)
    def pop(self, stackNum: int) -> int:
        if self.stacks[stackNum]:
            a=self.stacks[stackNum].pop()
        return -1

    def peek(self, stackNum: int) -> int:
        if self.stacks[stackNum]:
            return self.stacks[stackNum][-1]
        return -1
    def isEmpty(self, stackNum: int) -> bool:
        return False if self.stacks[stackNum] else True
# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
# leetcode submit region end(Prohibit modification and deletion)
