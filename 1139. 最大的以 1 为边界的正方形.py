# -*- coding: utf-8 -*-
from typing import List


# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0
# 。
#
#
#
#  示例 1：
#
#  输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
#
#
#  示例 2：
#
#  输入：grid = [[1,1,0,0]]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= grid.length <= 100
#  1 <= grid[0].length <= 100
#  grid[i][j] 为 0 或 1
#
#  Related Topics 动态规划
#  👍 71 👎 0

# 打擂台
# https://leetcode-cn.com/problems/largest-1-bordered-square/solution/dong-tai-gui-hua-yi-tang-bian-li-wan-cheng-by-lin-/
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        maxLen = 0
        u = [[0] * C for _ in range(R)]  # 上侧连续1的数目
        l = [[0] * C for _ in range(R)]  # 左侧连续1的数目
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                u[r][c] = 1
                l[r][c] = 1
                if r > 0:
                    u[r][c] += u[r - 1][c]
                if c > 0:
                    l[r][c] += l[r][c - 1]
                for k in range(min(l[r][c], u[r][c]), 0, -1):
                    if l[r - k + 1][c] >= k and u[r][c - k + 1] >= k:
                        maxLen = max(maxLen, k)
                        break
        return maxLen ** 2
