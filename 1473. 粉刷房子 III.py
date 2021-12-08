# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools

import bisect


# 在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不可以
# 被重新涂色。
#
#  我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区 [{1}, {2,2}
# , {3,3}, {2}, {1,1}] 。）
#
#  给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：
#
#
#  houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
#  cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
#
#
#  请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n
# = 2, target = 3
# 输出：9
# 解释：房子涂色方案为 [1,2,2,1,1]
# 此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
# 涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
#
#
#  示例 2：
#
#
# 输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n
# = 2, target = 3
# 输出：11
# 解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
# 此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
# 给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
#
#
#  示例 3：
#
#
# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5,
# n = 2, target = 5
# 输出：5
#
#
#  示例 4：
#
#
# 输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3,
#  target = 3
# 输出：-1
# 解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
#
#
#
#
#  提示：
#
#
#  m == houses.length == cost.length
#  n == cost[i].length
#  1 <= m <= 100
#  1 <= n <= 20
#  1 <= target <= m
#  0 <= houses[i] <= n
#  1 <= cost[i][j] <= 10^4
#
#  Related Topics 数组 动态规划 👍 157 👎 0

# https://leetcode-cn.com/problems/paint-house-iii/solution/fen-shua-fang-zi-iii-by-leetcode-solutio-powb/
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @functools.lru_cache(None)
        def f(i, j, k):
            '''
            :param i: 当前位置
            :param j: 当前颜色
            :param k: 当前街区数量
            :return:
            '''
            if k < 1:
                return float('inf')
            if i == 0:  # 边界条件
                if k != 1:
                    return float('inf')
                if houses[0] == 0:
                    return cost[0][j]
                else:
                    if houses[0] - 1 != j:  # houses[0]-1代表当前颜色，避免未染色，状态0的影响
                        return float('inf')
                    else:
                        return 0
            else:  # n为颜色的总数量
                if houses[i] == 0:
                    return min(min(f(i - 1, j_pre, k - 1) for j_pre in range(n) if j_pre != j), f(i - 1, j, k)) + \
                           cost[i][j]
                else:
                    if houses[i] - 1 != j:
                        return float('inf')
                    return min(min(f(i - 1, j_pre, k - 1) for j_pre in range(n) if j_pre != j), f(i - 1, j, k))

        a = min(f(len(houses) - 1, color, target) for color in range(n))
        return a if a != float('inf') else -1


# 优化版本
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        best = collections.defaultdict(lambda: (float('inf'), -1, float(
            'inf')))  # 默认字典best[i,k]=(first,first_j,second),first,second分别代表最少和第二少cost，first_j代表最少cost当前步颜色
        dp = collections.defaultdict(lambda: float('inf'))

        for i in range(m):
            for j in range(n):
                if houses[i] != 0 and houses[i] - 1 != j:
                    continue
                for k in range(1, i + 2):  # 最多分i+1个区
                    if i == 0:
                        if k != 1:
                            continue
                        if houses[0] == 0:
                            dp[i, j, k] = cost[i][j]
                        else:
                            dp[i, j, k] = 0
                    else:
                        dp[i, j, k] = dp[i - 1, j, k]
                        dp[i, j, k] = min(dp[i, j, k],
                                          best[i - 1, k - 1][0] if j != best[i - 1, k - 1][1] else best[i - 1, k - 1][
                                              2])
                        if houses[i] == 0:
                            dp[i, j, k] += cost[i][j]
                    first_i, _, second_i = best[i, k]
                    if dp[i, j, k] < first_i:  # 保留两个位置的情况下一般是不需要考虑是否相等的问题的
                        best[i, k] = (dp[i, j, k], j, first_i)
                    elif dp[i, j, k] < second_i:
                        best[i, k] = (first_i, _, dp[i, j, k])
        return best[m - 1, target][0] if best[m - 1, target][0] != float('inf') else -1


Solution().minCost([0, 2, 1, 2], [[1, 10], [10, 1], [10, 1], [1, 10]], 4, 2, 3)
