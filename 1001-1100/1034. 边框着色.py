# -*- coding: utf-8 -*-
from typing import List


# 给出一个二维整数网格 grid，网格中的每个值表示该位置处的网格块的颜色。
#
#  只有当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一连通分量。
#
#  连通分量的边界是指连通分量中的所有与不在分量中的正方形相邻（四个方向上）的所有正方形，或者在网格的边界上（第一行/列或最后一行/列）的所有正方形。
#
#  给出位于 (r0, c0) 的网格块和颜色 color，使用指定颜色 color 为所给网格块的连通分量的边界进行着色，并返回最终的网格 grid 。
#
#
#
#  示例 1：
#
#  输入：grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
# 输出：[[3, 3], [3, 2]]
#
#
#  示例 2：
#
#  输入：grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
# 输出：[[1, 3, 3], [2, 3, 3]]
#
#
#  示例 3：
#
#  输入：grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
# 输出：[[2, 2, 2], [2, 1, 2], [2, 2, 2]]
#
#
#
#  提示：
#
#
#  1 <= grid.length <= 50
#  1 <= grid[0].length <= 50
#  1 <= grid[i][j] <= 1000
#  0 <= r0 < grid.length
#  0 <= c0 < grid[0].length
#  1 <= color <= 1000
#
#
#
#  Related Topics 深度优先搜索
#  👍 24 👎 0


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        seen = {(r0, c0)}
        m = set()
        R, C = len(grid), len(grid[0])
        t = [[r0, c0]]
        while True:
            tree = []
            for r, c in t:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] != grid[r][c]:
                        m.add((r, c))
                    elif (nr, nc) not in seen:
                        tree.append([nr, nc])
                        seen.add((nr, nc))
            if not tree:
                break
            t = tree
        for r,c in m:
            grid[r][c]=color
        return grid