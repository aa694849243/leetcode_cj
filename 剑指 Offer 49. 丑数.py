#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq


# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
#
#
#  示例:
#
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
#  说明:
#
#
#  1 是丑数。
#  n 不超过1690。
#
#
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
#  Related Topics 哈希表 数学 动态规划 堆（优先队列）
#  👍 187 👎 0


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [1]
        while n > 0:
            a = heapq.heappop(q)
            while q and q[0] == a:
                heapq.heappop(q)
            heapq.heappush(q, a * 2)
            heapq.heappush(q, a * 3)
            heapq.heappush(q, a * 5)
            n -= 1
        return a


# 2动态规划

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if dp[i] == dp[i2] * 2:
                i2 += 1
            if dp[i] == dp[i3] * 3:
                i3 += 1
            if dp[i] == dp[i5] * 5:
                i5 += 1
        return dp[-1]


Solution().nthUglyNumber(12)
