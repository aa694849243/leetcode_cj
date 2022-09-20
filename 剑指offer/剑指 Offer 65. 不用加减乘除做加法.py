#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
#
#
#
#  示例:
#
#  输入: a = 1, b = 1
# 输出: 2
#
#
#
#  提示：
#
#
#  a, b 均可能是负数或 0
#  结果不会溢出 32 位整数
#
#  Related Topics 位运算 数学
#  👍 195 👎 0


class Solution:
    def add(self, a: int, b: int) -> int:
        return sum([a, b])


# 补码操作
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a &= x
        b &= x
        while b:
            c = (a & b) << 1  # 进位
            a ^= b  # 交错位
            b = c
        return a if a <= 0x7fffffff else ~(a ^ x)
