#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都
# 是O(1)。
#
#  若队列为空，pop_front 和 max_value 需要返回 -1
#
#  示例 1：
#
#  输入:
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,1,2]
#
#
#  示例 2：
#
#  输入:
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出: [null,-1,-1]
#
#
#
#
#  限制：
#
#
#  1 <= push_back,pop_front,max_value的总操作数 <= 10000
#  1 <= value <= 10^5
#
#  Related Topics 设计 队列 单调队列
#  👍 265 👎 0


class MaxQueue:

    def __init__(self):
        self.q = collections.deque()
        self.ma = collections.deque()

    def max_value(self) -> int:
        return self.ma[0] if self.ma else -1

    def push_back(self, value: int) -> None:
        while self.ma and value > self.ma[-1]:
            self.ma.pop()
        self.ma.append(value)
        self.q.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        a = self.q.popleft()
        if a == self.ma[0]:
            self.ma.popleft()
        return a
# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
obj.push_back(806)
obj.push_back(717)
obj.push_back(186)
obj.push_back(268)
obj.push_back(29)
obj.push_back(866)
obj.push_back(239)
obj.push_back(3)
obj.push_back(850)
param_1 = obj.max_value()
# param_3 = obj.pop_front()
# ["MaxQueue","push_back","push_back","push_back","push_back","push_back","push_back","push_back","push_back","push_back","max_value"]
# [[],[806],[717],[186],[268],[29],[866],[239],[3],[850],[]]