# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect
# 给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。
#
#  请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。
#
#  答案保证在 32 位有符号整数范围以内。
#
#
#
#  示例 1：
#
#
#
#  输入：houses = [1,4,8,10,20], k = 3
# 输出：5
# 解释：将邮筒分别安放在位置 3， 9 和 20 处。
# 每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。
#
#
#  示例 2：
#
#
#
#  输入：houses = [2,3,5,12,18], k = 2
# 输出：9
# 解释：将邮筒分别安放在位置 3 和 14 处。
# 每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。
#
#
#  示例 3：
#
#  输入：houses = [7,4,6,1], k = 1
# 输出：8
#
#
#  示例 4：
#
#  输入：houses = [3,6,14,10], k = 4
# 输出：0
#
#
#
#
#  提示：
#
#
#  n == houses.length
#  1 <= n <= 100
#  1 <= houses[i] <= 10^4
#  1 <= k <= n
#  数组 houses 中的整数互不相同。
#
#  Related Topics 数组 数学 动态规划 排序 👍 72 👎 0

from typing import List
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        cost = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    cost[i][j] = 0
                else:
                    cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]
        dp = [[float('inf')] * (k + 1) for _ in range(n)]  # dp[i][j]代表到i位置插j个邮筒，j从1开始
        for i in range(n):
            dp[i][1]=cost[0][i]
            for j in range(2, min(k, i + 1) + 1):  # j最多为k个或i+1(i从0开始）
                for i0 in range(i):
                    if dp[i0][j - 1] != float('inf'):
                        dp[i][j] = min(dp[i0][j - 1] + cost[i0 + 1][i], dp[i][j])
        return dp[-1][-1]