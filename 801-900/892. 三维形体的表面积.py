# 给你一个 n * n 的网格 grid ，上面放置着一些 1 x 1 x 1 的正方体。
#
#  每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
#
#  放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。
#
#  请你返回最终这些形体的总表面积。
#
#  注意：每个形体的底面也需要计入表面积中。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：grid = [[2]]
# 输出：10
#
#
#  示例 2：
#
#
# 输入：grid = [[1,2],[3,4]]
# 输出：34
#
#
#  示例 3：
#
#
# 输入：grid = [[1,0],[0,2]]
# 输出：16
#
#
#  示例 4：
#
#
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
#
#
#  示例 5：
#
#
# 输入：grid = [[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#
#
#
#
#  提示：
#
#
#  n == grid.length
#  n == grid[i].length
#  1 <= n <= 50
#  0 <= grid[i][j] <= 50
#
#  Related Topics 几何 数学
#  👍 146 👎 0

from typing import List


# 计算每个格子每个面贡献的表面积
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        R = len(grid)
        C = len(grid[0])
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    ans += 2
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C:
                            darea = grid[nr][nc]
                        else:
                            darea = 0
                        ans += max(grid[r][c] - darea, 0)
        return ans