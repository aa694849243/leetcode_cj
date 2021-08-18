#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 设计一个算法，算出 n 阶乘有多少个尾随零。
#
#  示例 1:
#
#  输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
#  示例 2:
#
#  输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
#  说明: 你算法的时间复杂度应为 O(log n) 。
#  Related Topics 数学
#  👍 48 👎 0


class Solution:
    def trailingZeroes(self, n: int) -> int:
        factor=5
        cnt=0
        while n>=factor:
            cnt+=n//factor
            factor*=5
        return cnt