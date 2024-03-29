# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
#
#  当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。
#
#  例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此
# 类推。请你计算出粉刷完所有房子最少的花费成本。
#
#  注意：
#
#  所有花费均为正整数。
#
#  示例：
#
#  输入: [[1,5,3],[2,9,4]]
# 输出: 5
# 解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5;
#      或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
#
#
#  进阶：
# 您能否在 O(nk) 的时间复杂度下解决此问题？
#  Related Topics 数组 动态规划 👍 104 👎 0


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m1, m2 = sorted(costs[0])[:2]
        l2, l1 = costs[0].index(m2), costs[0].index(m1)
        k = len(costs[0])
        dp = [(m1, l1), (m2, l2)]
        for li in costs[1:]:
            x1, x2 = float('inf'), float('inf')
            tmdp = dp[:]
            for j in range(k):
                if j == dp[0][1]:
                    tmpx = dp[1][0] + li[j]
                else:
                    tmpx = dp[0][0] + li[j]
                if tmpx < x1:
                    x2 = x1
                    x1 = tmpx
                    tmdp[1] = tmdp[0]
                    tmdp[0] = (tmpx, j)
                elif tmpx < x2:
                    x2 = tmpx
                    tmdp[1] = (tmpx, j)
            dp = tmdp
        return dp[0][0]
