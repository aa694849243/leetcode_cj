#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直
# 到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
#
#
#  示例 1:
#
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#
#
#
#  提示：
#
#
#  0 < grid.length <= 200
#  0 < grid[0].length <= 200
#
#  Related Topics 数组 动态规划 矩阵
#  👍 156 👎 0


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if r - 1 >= 0 and c - 1 >= 0:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
                elif r-1>=0:
                    dp[r][c]=dp[r-1][c]+grid[r][c]
                elif c-1>=0:
                    dp[r][c]=dp[r][c-1]+grid[r][c]
                else:
                    dp[r][c]=grid[r][c]
        return dp[-1][-1]
Solution().maxValue([[1,2,5],[3,2,1]])