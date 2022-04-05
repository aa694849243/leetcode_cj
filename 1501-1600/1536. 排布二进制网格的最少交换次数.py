#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
#
#  一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
#
#  请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
#
#  主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。
#
#
#
#  示例 1：
#
#
#
#  输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
# 输出：3
#
#
#  示例 2：
#
#
#
#  输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# 输出：-1
# 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
#
#
#  示例 3：
#
#
#
#  输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  n == grid.length
#  n == grid[i].length
#  1 <= n <= 200
#  grid[i][j] 要么是 0 要么是 1 。
#
#  Related Topics 贪心 数组 矩阵
#  👍 39 👎 0


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        grids = [[*map(str, row)] for row in grid]
        grids = [int(''.join(row), 2) for row in grids]
        res = 0
        for i in range(n := len(grids)):
            if i == n - 2:
                if grids[i] & 1 == 0:
                    return res
                elif grids[i + 1] & 1 == 0:
                    return res + 1
                return -1
            rd = n - i - 1
            mask = int('1' * rd, 2)
            if mask & grids[i] == 0:
                continue
            for j in range(i + 1, n):
                if mask & grids[j] == 0:
                    res += j - i
                    grids[i:j + 1] = [grids[j]] + grids[i:j]
                    break
            else:
                return -1


Solution().minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]])
