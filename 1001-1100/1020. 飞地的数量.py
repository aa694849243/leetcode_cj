# -*- coding: utf-8 -*-
from typing import List


# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。
#
#  移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。
#
#  返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。
#
#
#
#  示例 1：
#
#  输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#
#  示例 2：
#
#  输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：
# 所有 1 都在边界上或可以到达边界。
#
#
#
#  提示：
#
#
#  1 <= A.length <= 500
#  1 <= A[i].length <= 500
#  0 <= A[i][j] <= 1
#  所有行的大小都相同
#
#  Related Topics 深度优先搜索
#  👍 46 👎 0


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        orgin = -1
        for i in range(R := len(grid)):
            for j in range(C := len(grid[0])):
                num = i * C + j
                if grid[i][j] == 1 and (i == 0 or i == R - 1 or j == 0 or j == C - 1):
                    union(orgin, num)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(1, R - 1):
            for j in range(1, C - 1):
                num = i * C + j
                if grid[i][j] != 1:
                    continue
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    nnum = ni * C + nj
                    if grid[ni][nj] == 1 and find(nnum) == -1:
                        union(orgin, num)
                    elif grid[ni][nj] == 1 and find(num)==-1:
                        union(num, nnum)
                    elif grid[ni][nj]==1:
                        union(nnum,num)
        ans = 0
        for i in range(1, R - 1):
            for j in range(1, C - 1):
                num = i * C + j
                if grid[i][j] == 1 and find(num) != -1:
                    ans += 1
        return ans


Solution().numEnclaves([[0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]])