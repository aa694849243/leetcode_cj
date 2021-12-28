#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你一个由若干 0 和 1 组成的二维网格 grid ，其中 0 表示水，而 1 表示陆地。岛屿由水平方向或竖直方向上相邻的 1 （陆地）连接形成。
#
#  如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。
#
#  一天内，可以将任何单个陆地单元（1）更改为水单元（0）。
#
#  返回使陆地分离的最少天数。
#
#
#
#  示例 1：
#
#
#
#  输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：2
# 解释：至少需要 2 天才能得到分离的陆地。
# 将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
#
#
#  示例 2：
#
#  输入：grid = [[1,1]]
# 输出：2
# 解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
#
#
#  示例 3：
#
#  输入：grid = [[1,0,1,0]]
# 输出：0
#
#
#  示例 4：
#
#  输入：grid = [[1,1,0,1,1],
#              [1,1,1,1,1],
#              [1,1,0,1,1],
#              [1,1,0,1,1]]
# 输出：1
#
#
#  示例 5：
#
#  输入：grid = [[1,1,0,1,1],
#              [1,1,1,1,1],
#              [1,1,0,1,1],
#              [1,1,1,1,1]]
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= grid.length, grid[i].length <= 30
#  grid[i][j] 为 0 或 1
#
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 强连通分量
#  👍 31 👎 0


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = set()
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    m.add((r, c))
        vis = set()
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def find(r, c):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in vis:
                    vis.add((nr, nc))
                    find(nr, nc)

        for r, c in m:  # 检查是否连通，不连通直接返回0
            sr, sc = r, c
            vis.add((sr, sc))
            find(r, c)
            if len(vis) != len(m):
                return 0
            # if len(vis)==1:
            #     return 1
            break

        dfn, low = collections.defaultdict(lambda: -1), collections.defaultdict(lambda: -1)
        self.flag = False

        def tarjan(parent, node, timestamp):
            r, c = node[0], node[1]
            dfn[r, c] = timestamp
            low[r, c] = timestamp
            if (r, c) != (sr, sc):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) == parent or nr >= R or nr < 0 or nc < 0 or nc >= C or grid[nr][nc] != 1:
                        continue
                    if low[nr, nc] == -1:
                        tarjan((r, c), (nr, nc), timestamp + 1)
                        if low[nr, nc] >= dfn[r, c]:
                            self.flag = True
                        low[r, c] = min(low[r, c], low[nr, nc])
                    else:
                        low[r, c] = min(low[r, c], low[nr, nc])
                return low[r, c]
            else:
                cnt = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr >= R or nr < 0 or nc < 0 or nc >= C or grid[nr][nc] != 1 or low[nr, nc] != -1:
                        continue
                    tarjan((r, c), (nr, nc), timestamp + 1)
                    cnt += 1
                if cnt >= 2:
                    self.flag = True

        tarjan((-1, -1), (sr, sc), 0)
        return 1 if self.flag else min(2, len(vis))


print(Solution().minDays([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
