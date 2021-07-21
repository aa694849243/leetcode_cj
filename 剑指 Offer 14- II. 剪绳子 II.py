#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1]
#  。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘
# 积是18。
#
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
#
#
#  示例 1：
#
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
#
#  示例 2:
#
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
#
#
#
#  提示：
#
#
#  2 <= n <= 1000
#
#
#  注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
#  Related Topics 数学 动态规划
#  👍 125 👎 0


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        mod = 10 ** 9 + 7
        rem = n % 3
        if rem == 1:
            rem = 4
            n -= 4
        a = n // 3
        return (pow(3, a, mod) + max(rem,1)) % mod
