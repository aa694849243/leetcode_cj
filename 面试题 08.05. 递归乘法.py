#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。
#
#  示例1:
#
#
#  输入：A = 1, B = 10
#  输出：10
#
#
#  示例2:
#
#
#  输入：A = 3, B = 4
#  输出：12
#
#
#  提示:
#
#
#  保证乘法范围不会溢出
#
#  Related Topics 位运算 递归 数学
#  👍 44 👎 0


class Solution:
    def multiply(self, A: int, B: int) -> int:
        def rec(a, b):
            if b == 1:
                return a
            ans = rec(a, b // 2)
            if b % 2:
                return ans + ans + rec(a, 1)
            else:
                return ans + ans

        return rec(A, B)


class Solution:
    def multiply(self, A: int, B: int) -> int:
        ans = 0
        while B:
            if B & 1:
                ans += A
            B>>=1
            A<<=1
        return ans