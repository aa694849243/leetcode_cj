#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
import functools
from typing import List
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
#
#
#
#  示例 1：
#
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#
#
#  示例 2：
#
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#
#  示例 3：
#
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#
#
#
#  提示：
#
#
#  -100.0 < x < 100.0
#  -231 <= n <= 231-1
#  -104 <= xn <= 104
#
#
#
#
#  注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/
#  Related Topics 递归 数学
#  👍 176 👎 0


class Solution:
    def myPow(self, x: float, n: int) -> float:
        @functools.lru_cache(None)
        def dp(x,n):
            if n==0:
                return 1
            elif n==1:
                return x
            return dp(x,n//2)*dp(x,n-n//2)

        return dp(x,n) if n>=0 else 1/dp(x,-n)