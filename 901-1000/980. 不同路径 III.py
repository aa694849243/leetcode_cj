# -*- coding: utf-8 -*-
import collections, heapq, itertools
import functools
from typing import List


# 在二维网格 grid 上，有 4 种类型的方格：
#
#
#  1 表示起始方格。且只有一个起始方格。
#  2 表示结束方格，且只有一个结束方格。
#  0 表示我们可以走过的空方格。
#  -1 表示我们无法跨越的障碍。
#
#
#  返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
#
#  每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。
#
#
#
#  示例 1：
#
#  输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# 输出：2
# 解释：我们有以下两条路径：
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
#  示例 2：
#
#  输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# 输出：4
# 解释：我们有以下四条路径：
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
#  示例 3：
#
#  输入：[[0,1],[2,0]]
# 输出：0
# 解释：
# 没有一条路能完全穿过每一个空的方格一次。
# 请注意，起始和结束方格可以位于网格中的任意位置。
#
#
#
#
#  提示：
#
#
#  1 <= grid.length * grid[0].length <= 20
#
#  Related Topics 深度优先搜索 回溯算法
#  👍 138 👎 0

# dfs
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def neighbors(i, j):
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:  # 起点值为1，避免回溯到起点可以%2
                    yield nr, nc

        todo = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] != -1: todo += 1
                if grid[r][c] == 1:
                    sr, sc = r, c
                if grid[r][c] == 2:
                    tr, tc = r, c
        self.ans = 0

        def dp(r, c, todo):
            todo -= 1
            if todo < 0: return
            if (r, c) == (tr, tc) and todo == 0:
                self.ans += 1
            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dp(nr, nc, todo)
            grid[r][c] = 0

        dp(sr, sc, todo)
        return self.ans


# 记忆化 二进制状态
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def neighbors(i, j):
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:  # 起点值为1，避免回溯到起点可以%2
                    yield nr, nc

        target = 0

        def code(r, c):
            return 1 << (r * C + c)

        target = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] != -1: target |= code(r, c)
                if grid[r][c] == 1:
                    sr, sc = r, c
                if grid[r][c] == 2:
                    tr, tc = r, c
        self.ans = 0

        @functools.lru_cache(None)
        def dp(r, c, todo):
            todo ^= code(r, c)
            if todo == 0:
                return +((r, c) == (tr, tc))
            ans = 0
            for nr, nc in neighbors(r, c):
                if code(nr, nc) & todo:
                    ans += dp(nr, nc, todo)
            return ans

        return dp(sr, sc, target)
