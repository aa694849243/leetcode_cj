#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定两个整型数字 N 与 M，以及表示比特位置的 i 与 j（i <= j，且从 0 位开始计算）。
#
#  编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，不足之处用 0 补齐。具体插入过程如图所示。
#
#
#
#  题目保证从 i 位到 j 位足以容纳 M， 例如： M = 10011，则 i～j 区域至少可容纳 5 位。
#
#
#
#  示例1:
#
#
#  输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
#  输出：N = 1100(10001001100)
#
#
#  示例2:
#
#
#  输入： N = 0, M = 31(11111), i = 0, j = 4
#  输出：N = 31(11111)
#
#  Related Topics 位运算
#  👍 34 👎 0


class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        n = str(bin(N))[2:]
        m = str(bin(M))[2:]
        if len(m) < j - i + 1:
            m = '0' * (j - i + 1-len(m)) + m
        n = n[::-1]
        m = m[::-1]
        n = n[:i] + m + n[j + 1:]
        return int(n[::-1], 2)


Solution().insertBits(2032243561, 10, 24, 29)
