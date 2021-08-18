#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。
#
#  示例:
#
#  输入: 25
# 输出: 9
# 解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
#
#  提示：
#
#
#  n <= 10^9
#
#  Related Topics 递归 数学 动态规划
#  👍 40 👎 0


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        if n <= 1:
            return 0
        if n <= 11:
            return 1
        i = 1
        a, b = 0, 0
        cnt = 0
        while i <= n:
            a = n // i
            b = n % i
            cnt += (a + 7) // 10 * i + (a % 10 == 2) * (b + 1)
            i *= 10
        return cnt
