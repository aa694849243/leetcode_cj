# -*- coding: utf-8 -*-
# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
#
#
#
#  示例 1：
#
#  输入：matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 输出：15
# 解释：
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
#
#
#  示例 2：
#
#  输入：matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 300
#  1 <= arr[0].length <= 300
#  0 <= arr[i][j] <= 1
#
#  Related Topics 数组 动态规划
#  👍 157 👎 0
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    #dp[i][j]代表以i,j为右下角，正方形最大边长，此边长刚好也等于以该点为右下角正方形的数量
                ans+=dp[i][j]
        return ans



Solution().countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]])
