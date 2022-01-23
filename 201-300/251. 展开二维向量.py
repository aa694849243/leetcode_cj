# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 next 和 hasNext 两种操作。
#
#
#
#  示例：
#
#
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
#
# iterator.next(); // 返回 1
# iterator.next(); // 返回 2
# iterator.next(); // 返回 3
# iterator.hasNext(); // 返回 true
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 4
# iterator.hasNext(); // 返回 false
#
#
#
#
#  注意：
#
#
#  请记得 重置 在 Vector2D 中声明的类变量（静态变量），因为类变量会 在多个测试用例中保持不变，影响判题准确。请 查阅 这里。
#  你可以假定 next() 的调用总是合法的，即当 next() 被调用时，二维向量总是存在至少一个后续元素。
#
#
#
#
#  进阶：尝试在代码中仅使用 C++ 提供的迭代器 或 Java 提供的迭代器。
#  Related Topics 设计 数组 双指针 迭代器 👍 51 👎 0


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.x = 0
        self.y = 0

    def next(self) -> int:
        while not self.vec[self.x]:
            self.x += 1
        a = self.vec[self.x][self.y]
        self.y += 1
        if self.y == len(self.vec[self.x]):
            self.x += 1
            self.y = 0
        return a

    def hasNext(self) -> bool:
        while self.x < len(self.vec) and not self.vec[self.x]:
            self.x += 1
        return self.x < len(self.vec)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
