# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个非空 01 二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。
#
#  请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。
#
#
#
#  示例 1：
#
#  11000
# 11000
# 00011
# 00011
#
#
#  给定上图，返回结果 1 。
#
#  示例 2：
#
#  11011
# 10000
# 00001
# 11011
#
#  给定上图，返回结果 3 。
#
# 注意：
#
#  11
# 1
#
#
#  和
#
#   1
# 11
#
#
#  是不同的岛屿，因为我们不考虑旋转、翻转操作。
#
#
#
#  提示：二维数组每维的大小都不会超过 50 。
#  Related Topics 深度优先搜索 广度优先搜索 并查集 哈希表 哈希函数 👍 104 👎 0

# 网格散列
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])
        visted = set()

        def dfs(r, c):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in visted:
                    visted.add((nr, nc))
                    paths.append([nr, nc])
                    dfs(nr, nc)

        def hash(lst):
            sr, sc = lst[0]
            for i in range(1, len(lst)):
                lst[i][0] -= sr
                lst[i][1] -= sc
            lst[0] = [0, 0]
            ans = ''
            for x, y in lst:
                ans += str(x) + str(y)
            return ans

        res = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in visted:
                    visted.add((r, c))
                    paths = [[r, c]]
                    dfs(r, c)
                    paths.sort()
                    res.add(hash(paths))
        return len(res)


Solution().numDistinctIslands([[0, 1]])
