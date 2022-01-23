# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 你是个房地产开发商，想要选择一片空地 建一栋大楼。你想把这栋大楼够造在一个距离周边设施都比较方便的地方，通过调研，你希望从它出发能在 最短的距离和 内抵达周
# 边全部的建筑物。请你计算出这个最佳的选址到周边全部建筑物的 最短距离和。
#
#
#
#  提示：
#
#  你只能通过向上、下、左、右四个方向上移动。
#
#  给你一个由 0、1 和 2 组成的二维网格，其中：
#
#
#  0 代表你可以自由通过和选择建造的空地
#  1 代表你无法通行的建筑物
#  2 代表你无法通行的障碍物
#
#
#
#
#  示例：
#
#  输入：[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 输出：7
# 解析：
# 给定三个建筑物 (0,0)、(0,4) 和 (2,2) 以及一个位于 (0,2) 的障碍物。
# 由于总距离之和 3+3+1=7 最优，所以位置 (1,2) 是符合要求的最优地点，故返回7。
#
#
#
#
#  注意：
#
#
#  题目数据保证至少存在一栋建筑物，如果无法按照上述规则返回建房地点，则请你返回 -1。
#
#  Related Topics 广度优先搜索 数组 矩阵 👍 111 👎 0


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])

        sr = []
        target = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    sr.append((r, c))
                elif grid[r][c] == 1:
                    target.append((r, c))

        m = collections.defaultdict(lambda: float('inf'))

        def find(i, j):
            visted = {(i, j)}
            t = [(i, j)]
            step = 0
            while 1:
                tree = []
                step += 1
                for r, c in t:
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 2 and (nr, nc) not in visted:
                            visted.add((nr, nc))
                            if grid[nr][nc] == 0:
                                m[nr, nc, i, j] = step
                                tree.append((nr, nc))
                if not tree:
                    break
                t = tree
            return m  # m保存源节点到目标节点的距离

        ans = float('inf')
        for i, j in target:
            find(i, j)
        for r, c in sr:
            res = 0
            for i, j in target:
                res += m[r, c, i, j]
                if res == float('inf'):
                    break
            else:
                ans = min(res, ans)
        return ans if ans != float('inf') else -1


Solution().shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
