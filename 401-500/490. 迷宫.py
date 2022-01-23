# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 由空地（用 0 表示）和墙（用 1 表示）组成的迷宫 maze 中有一个球。球可以途经空地向 上、下、左、右 四个方向滚动，且在遇到墙壁前不会停止滚动。当球
# 停下时，可以选择向下一个方向滚动。
#
#
#
#  给你一个大小为 m x n 的迷宫 maze ，以及球的初始位置 start 和目的地 destination ，其中 start = [
# startrow, startcol] 且 destination = [destinationrow, destinationcol] 。请你判断球能否在目的地停下：如果可以
# ，返回 true ；否则，返回 false 。
#
#  你可以 假定迷宫的边缘都是墙壁（参考示例）。
#
#
#
#  示例 1：
#
#
# 输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
# start = [0,4], destination = [4,4]
# 输出：true
# 解释：一种可能的路径是 : 左 -> 下 -> 左 -> 下 -> 右 -> 下 -> 右。
#
#
#  示例 2：
#
#
# 输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
# start = [0,4], destination = [3,2]
# 输出：false
# 解释：不存在能够使球停在目的地的路径。注意，球可以经过目的地，但无法在那里停驻。
#
#
#  示例 3：
#
#
# 输入：maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],
# start = [4,3], destination = [0,1]
# 输出：false
#
#
#
#
#  提示：
#
#
#  m == maze.length
#  n == maze[i].length
#  1 <= m, n <= 100
#  maze[i][j] is 0 or 1.
#  start.length == 2
#  destination.length == 2
#  0 <= startrow, destinationrow <= m
#  0 <= startcol, destinationcol <= n
#  球和目的地都在空地上，且初始时它们不在同一位置
#  迷宫 至少包括 2 块空地
#
#
#
#
#  Related Topics 深度优先搜索 广度优先搜索 图 👍 127 👎 0


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visted = {tuple(start)}
        sr, sc = start
        t = [(sr, sc)]
        R, C = len(maze), len(maze[0])
        while 1:
            tree = []
            for r, c in t:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    while 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != 1:
                        nr += dr
                        nc += dc
                    nr -= dr
                    nc -= dc
                    if [nr, nc] == destination:
                        return True
                    if (nr, nc) not in visted:
                        visted.add((nr, nc))
                        tree.append((nr,nc))
            if not tree:
                break
            t = tree
        return False


Solution().hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4],
                   [4, 4])
