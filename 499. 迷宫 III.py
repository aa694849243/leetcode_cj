#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
from typing import List


# 由空地和墙组成的迷宫中有一个球。球可以向上（u）下（d）左（l）右（r）四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。迷宫中还有
# 一个洞，当球运动经过洞时，就会掉进洞里。
#
#  给定球的起始位置，目的地和迷宫，找出让球以最短距离掉进洞里的路径。 距离的定义是球从起始位置（不包括）到目的地（包括）经过的空地个数。通过'u', 'd'
# , 'l' 和 'r'输出球的移动方向。 由于可能有多条最短路径， 请输出字典序最小的路径。如果球无法进入洞，输出"impossible"。
#
#  迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。
#
#
#
#  示例1:
#
#  输入 1: 迷宫由以下二维数组表示
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# 输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
# 输入 3: 洞的位置 (rowHole, colHole) = (0, 1)
#
# 输出: "lul"
#
# 解析: 有两条让球进洞的最短路径。
# 第一条路径是 左 -> 上 -> 左, 记为 "lul".
# 第二条路径是 上 -> 左, 记为 'ul'.
# 两条路径都具有最短距离6, 但'l' < 'u'，故第一条路径字典序更小。因此输出"lul"。
#
#
#
#  示例 2:
#
#  输入 1: 迷宫由以下二维数组表示
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# 输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
# 输入 3: 洞的位置 (rowHole, colHole) = (3, 0)
#
# 输出: "impossible"
#
# 示例: 球无法到达洞。
#
#
#
#
#
#  注意:
#
#
#  迷宫中只有一个球和一个目的地。
#  球和洞都在空地上，且初始时它们不在同一位置。
#  给定的迷宫不包括边界 (如图中的红色矩形), 但你可以假设迷宫的边缘都是墙壁。
#  迷宫至少包括2块空地，行数和列数均不超过30。
#
#  Related Topics 深度优先搜索 广度优先搜索 图 最短路 堆（优先队列）
#  👍 46 👎 0


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dirs2 = ['u', 'r', 'd', 'l']
        res = []
        visted = set()
        R, C = len(maze), len(maze[0])
        sr, sc = ball
        q = [(0, '', sr, sc)]
        while q:
            dis, path, r, c = heapq.heappop(q)
            visted.add((r,c))
            if res and dis > res[0][0]:
                break
            for di in range(4):
                dr, dc = dirs[di]
                npath = path + dirs2[di]
                step = 1
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C or maze[nr][nc] == 1:
                    continue
                while 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == 0:
                    if [nr, nc] == hole:
                        res.append((dis + step, npath))
                        break
                    step += 1
                    nr += dr
                    nc += dc
                if [nr, nc] != hole:
                    nr -= dr
                    nc -= dc
                    step -= 1
                    if (nr, nc) not in visted:
                        heapq.heappush(q, (dis + step, npath, nr, nc))
        return sorted(res)[0][1] if res else 'impossible'


Solution().findShortestWay(
    [[0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
     [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]], [2, 4], [7, 6])
