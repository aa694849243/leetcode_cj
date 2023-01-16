# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始的二维整数数组 grid ，数组大小为 m x n 。每个单元格都是两个值之一：
#
#
#  0 表示一个 空 单元格，
#  1 表示一个可以移除的 障碍物 。
#
#
#  你可以向上、下、左、右移动，从一个空单元格移动到另一个空单元格。
#
#  现在你需要从左上角 (0, 0) 移动到右下角 (m - 1, n - 1) ，返回需要移除的障碍物的 最小 数目。
#
#
#
#  示例 1：
#
#
#
#
# 输入：grid = [[0,1,1],[1,1,0],[1,1,0]]
# 输出：2
# 解释：可以移除位于 (0, 1) 和 (0, 2) 的障碍物来创建从 (0, 0) 到 (2, 2) 的路径。
# 可以证明我们至少需要移除两个障碍物，所以返回 2 。
# 注意，可能存在其他方式来移除 2 个障碍物，创建出可行的路径。
#
#
#  示例 2：
#
#
#
#
# 输入：grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
# 输出：0
# 解释：不移除任何障碍物就能从 (0, 0) 到 (2, 4) ，所以返回 0 。
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 10⁵
#  2 <= m * n <= 10⁵
#  grid[i][j] 为 0 或 1
#  grid[0][0] == grid[m - 1][n - 1] == 0
#
#
#  Related Topics 广度优先搜索 图 数组 矩阵 最短路 堆（优先队列）
#  👍 36 👎 0
import collections
import heapq

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dis_matrix = [[float('inf')] * C for _ in range(R)]
        dis_matrix[0][0] = 0
        q = [(0, 0, 0)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            dis, x, y = heapq.heappop(q)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and dis + grid[nx][ny] < dis_matrix[nx][ny]:
                    dis_matrix[nx][ny] = dis + grid[nx][ny]
                    heapq.heappush(q, (dis_matrix[nx][ny], nx, ny))
        return dis_matrix[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimumObstacles([[0],[0]]))