#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 你被给定一个 m × n 的二维网格 rooms ，网格中有以下三种可能的初始化值：
#
#
#  -1 表示墙或是障碍物
#  0 表示一扇门
#  INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647
# 的。
#
#
#  你要给每个空房间位上填上该房间到 最近门的距离 ，如果无法到达门，则填 INF 即可。
#
#
#
#  示例 1：
#
#
# 输入：rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1]
# ,[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# 输出：[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
#
#
#  示例 2：
#
#
# 输入：rooms = [[-1]]
# 输出：[[-1]]
#
#
#  示例 3：
#
#
# 输入：rooms = [[2147483647]]
# 输出：[[2147483647]]
#
#
#  示例 4：
#
#
# 输入：rooms = [[0]]
# 输出：[[0]]
#
#
#
#
#  提示：
#
#
#  m == rooms.length
#  n == rooms[i].length
#  1 <= m, n <= 250
#  rooms[i][j] 是 -1、0 或 231 - 1
#
#  Related Topics 广度优先搜索 数组 矩阵
#  👍 186 👎 0


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        doors = []
        R, C = len(rooms), len(rooms[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    doors.append((r, c))

        def bfs(i, j):
            visted = {(i, j)}
            t = [(i, j)]
            step = 0
            while 1:
                tree = []
                step += 1
                for r, c in t:
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and rooms[nr][nc] > 0 and (nr, nc) not in visted:
                            visted.add((nr, nc))
                            rooms[nr][nc] = min(rooms[nr][nc], step)
                            tree.append((nr, nc))
                if not tree:
                    break
                t = tree

        for i, j in doors:
            bfs(i, j)
