#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定
# ）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如
# enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。
#
#  enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。
#
#  dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。
#
#  示例1:
#
#   输入：
# ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"
# ]
# [[], [[0, 0]], [[1, 0]], [], [], []]
#  输出：
# [null,null,null,[0,0],[-1,-1],[1,0]]
#
#
#  示例2:
#
#   输入：
# ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "
# dequeueAny"]
# [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
#  输出：
# [null,null,null,null,[2,1],[0,0],[1,0]]
#
#
#  说明:
#
#
#  收纳所的最大容量为20000
#
#  Related Topics 设计 队列
#  👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class AnimalShelf:

    def __init__(self):
        self.q = [[], []]
        self.s = []
        self.m = set()

    def enqueue(self, animal: List[int]) -> None:
        a, b = animal
        self.q[b].append(a)
        self.s.append((a, b))

    def dequeueAny(self) -> List[int]:
        while self.s and tuple(self.s[0]) in self.m:
            self.s.pop(0)
        if not self.s:
            return [-1, -1]
        a, b = self.s.pop(0)
        self.q[b].pop(0)
        return [a, b]

    def dequeueDog(self) -> List[int]:
        if not self.q[1]:
            return [-1, -1]
        a = self.q[1].pop(0)
        self.m.add((a, 1))
        return [a, 1]

    def dequeueCat(self) -> List[int]:
        if not self.q[0]:
            return [-1, -1]
        a = self.q[0].pop(0)
        self.m.add((a, 0))
        return [a, 0]

# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
