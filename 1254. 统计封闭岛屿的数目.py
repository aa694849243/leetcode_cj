# -*- coding: utf-8 -*-
from typing import List


# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
#
#  我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
#
#  如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。
#
#  请返回封闭岛屿的数目。
#
#
#
#  示例 1：
#
#
#
#  输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1
# ,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
#
#  示例 2：
#
#
#
#  输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#
#
#  示例 3：
#
#  输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= grid.length, grid[0].length <= 100
#  0 <= grid[i][j] <=1
#
#  Related Topics 深度优先搜索
#  👍 80 👎 0


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r == R-1 or c == C-1 or r==0 or c==0:
                return False
            grid[r][c] = 2
            a = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 0:
                    if not dfs(nr, nc):
                        a = False
            return a

        ans = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        ans += 1
        return ans           
Solution().closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1]])
