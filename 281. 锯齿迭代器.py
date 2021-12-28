#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。
#
#  示例:
#
#  输入:
# v1 = [1,2]
# v2 = [3,4,5,6]
#
# 输出: [1,3,2,4,5,6]
#
# 解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
#      next 函数返回值的次序应依次为: [1,3,2,4,5,6]。
#
#  拓展：假如给你 k 个一维向量呢？你的代码在这种情况下的扩展性又会如何呢?
#
#  拓展声明：
#  “锯齿” 顺序对于 k > 2 的情况定义可能会有些歧义。所以，假如你觉得 “锯齿” 这个表述不妥，也可以认为这是一种 “循环”。例如：
#
#  输入:
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# 输出: [1,4,8,2,5,9,3,6,7].
#
#  Related Topics 设计 队列 数组 迭代器
#  👍 49 👎 0


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.mat = [v1, v2]
        self.x = 0
        self.y = 0
        self.limy = max(len(self.mat[0]), len(self.mat[1]))
        while self.y >= len(self.mat[self.x]) and self.y < self.limy:
            if self.x == 1:
                self.y += 1
            self.x = (self.x + 1) % 2
    def next(self) -> int:
        a = self.mat[self.x][self.y]
        while self.y < self.limy:
            if self.x == 1:
                self.y += 1
            self.x = (self.x + 1) % 2
            while self.y >= len(self.mat[self.x]) and self.y < self.limy:
                if self.x == 1:
                    self.y += 1
                self.x = (self.x + 1) % 2
            break
        return a

    def hasNext(self) -> bool:
        return self.y < self.limy


b = ZigzagIterator([1, 2], [3, 4, 5, 6])
while b.hasNext():
    c = b.next()
