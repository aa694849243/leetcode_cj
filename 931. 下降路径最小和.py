# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
#
#  下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第
# 一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1
# , col + 1) 。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：下面是两条和最小的下降路径，用加粗标注：
# [[2,1,3],      [[2,1,3],
#  [6,5,4],       [6,5,4],
#  [7,8,9]]       [7,8,9]]
#
#
#  示例 2：
#
#
# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：下面是一条和最小的下降路径，用加粗标注：
# [[-19,57],
#  [-40,-5]]
#
#
#  示例 3：
#
#
# 输入：matrix = [[-48]]
# 输出：-48
#
#
#
#
#  提示：
#
#
#  n == matrix.length
#  n == matrix[i].length
#  1 <= n <= 100
#  -100 <= matrix[i][j] <= 100
#
#  Related Topics 动态规划
#  👍 88 👎 0


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = {}

        def dp(i, j):
            if i == 0:
                return matrix[i][j]
            if (i, j) in m:
                return m[i, j]
            ans = float('inf')
            for k in {max(j - 1, 0), j, min(n - 1, j + 1)}:
                ans = min(ans, dp(i - 1, k) + matrix[i][j])
            m[i, j] = ans
            return ans

        return min(dp(n - 1, x) for x in range(n))


# 自底向上 直接修改原数组
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        while len(matrix) >= 2:
            row = matrix.pop()
            for i in range(n):
                matrix[-1][i] += min({row[i], row[min(i + 1, n - 1)], row[max(0, i - 1)]})
        return min(matrix[0])


Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
