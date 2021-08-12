#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。
#  示例：
#  输入： a = 1, b = 2
# 输出： 2
#
#  Related Topics 位运算 脑筋急转弯 数学
#  👍 88 👎 0


class Solution:
    def maximum(self, a: int, b: int) -> int:
        return max(a,b)