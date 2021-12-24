# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 整数可以被看作是其因子的乘积。
#
#  例如：
#
#  8 = 2 x 2 x 2;
#   = 2 x 4.
#
#  请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。
#
#  注意：
#
#
#  你可以假定 n 为永远为正数。
#  因子必须大于 1 并且小于 n。
#
#
#  示例 1：
#
#  输入: 1
# 输出: []
#
#
#  示例 2：
#
#  输入: 37
# 输出: []
#
#  示例 3：
#
#  输入: 12
# 输出:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
#
#  示例 4:
#
#  输入: 32
# 输出:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
#
#  Related Topics 数组 回溯 👍 100 👎 0


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def dfs(x, l):
            res = []
            for i in range(l, int(x ** .5) + 1):
                if x % i == 0:
                    res.append([i, x // i])
                    for nxt in dfs(x // i, i):
                        sub = [i] + nxt
                        res.append(sub)
            return res

        return dfs(n, 2)


Solution().getFactors(8)
