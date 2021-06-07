# -*- coding: utf-8 -*-
from typing import List


# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
#
#  二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求
# ：
#
#
#  路径途经的所有单元格都的值都是 0 。
#  路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
#
#
#  畅通路径的长度 是该路径途经的单元格总数。
#
#
#
#  示例 1：
#
#
# 输入：grid = [[0,1],[1,0]]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
# 输出：4
#
#
#  示例 3：
#
#
# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
#
#
#
#
#  提示：
#
#
#  n == grid.length
#  n == grid[i].length
#  1 <= n <= 100
#  grid[i][j] 为 0 或 1
#
#  Related Topics 广度优先搜索
#  👍 103 👎 0


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        seen = set()
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]
        t = [(0, 0)]
        step = 1
        R, C = len(grid), len(grid[0])
        if (R,C)==(1,1):
            return 1
        while True:
            tree = []
            for r, c in t:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen and grid[nr][nc] == 0:
                        if (nr, nc) == (R - 1, C - 1):
                            return step + 1
                        seen.add((nr, nc))
                        tree.append((nr, nc))
            step += 1
            if not tree:
                break
            t = tree
        return -1
