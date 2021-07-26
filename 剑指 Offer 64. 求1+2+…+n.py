#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools


# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#
#
#
#  示例 1：
#
#  输入: n = 3
# 输出: 6
#
#
#  示例 2：
#
#  输入: n = 9
# 输出: 45
#
#
#
#
#  限制：
#
#
#  1 <= n <= 10000
#
#  Related Topics 位运算 递归 脑筋急转弯
#  👍 348 👎 0


class Solution:
    def sumNums(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n):
            if n == 1:
                return 1
            return dfs(n - 1) + n

        return dfs(n)


# 俄罗斯农民乘法
# https://leetcode-cn.com/problems/qiu-12n-lcof/solution/qiu-12n-by-leetcode-solution/
class Solution:
    def sumNums(self, n: int) -> int:  # 数据范围，14位展开
        self.ans = 0

        def cal(a, b):
            if a & 1:
                self.ans += b

        a, b = n, n + 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        cal(a, b)
        a >>= 1
        b <<= 1
        return self.ans >> 1
