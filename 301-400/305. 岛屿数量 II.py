#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你一个大小为 m x n 的二进制网格 grid 。网格表示一个地图，其中，0 表示水，1 表示陆地。最初，grid 中的所有单元格都是水单元格（即，所有
# 单元格都是 0）。
#
#  可以通过执行 addLand 操作，将某个位置的水转换成陆地。给你一个数组 positions ，其中 positions[i] = [ri, ci] 是
# 要执行第 i 次操作的位置 (ri, ci) 。
#
#  返回一个整数数组 answer ，其中 answer[i] 是将单元格 (ri, ci) 转换为陆地后，地图中岛屿的数量。
#
#  岛屿 的定义是被「水」包围的「陆地」，通过水平方向或者垂直方向上相邻的陆地连接而成。你可以假设地图网格的四边均被无边无际的「水」所包围。
#
#
#  示例 1：
#
#
# 输入：m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
# 输出：[1,1,2,3]
# 解释：
# 起初，二维网格 grid 被全部注入「水」。（0 代表「水」，1 代表「陆地」）
# - 操作 #1：addLand(0, 0) 将 grid[0][0] 的水变为陆地。此时存在 1 个岛屿。
# - 操作 #2：addLand(0, 1) 将 grid[0][1] 的水变为陆地。此时存在 1 个岛屿。
# - 操作 #3：addLand(1, 2) 将 grid[1][2] 的水变为陆地。此时存在 2 个岛屿。
# - 操作 #4：addLand(2, 1) 将 grid[2][1] 的水变为陆地。此时存在 3 个岛屿。
#
#
#  示例 2：
#
#
# 输入：m = 1, n = 1, positions = [[0,0]]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  1 <= m, n, positions.length <= 104
#  1 <= m * n <= 104
#  positions[i].length == 2
#  0 <= ri < m
#  0 <= ci < n
#
#
#
#
#  进阶：你可以设计一个时间复杂度 O(k log(mn)) 的算法解决此问题吗？（其中 k == positions.length）
#  Related Topics 并查集 数组
#  👍 111 👎 0

class unionFind:
    def __init__(self, n):
        self.vcount = n
        self.f = {}
        self.sizes = collections.defaultdict(lambda: 1)

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a != b:
            self.f[b] = a
        else:
            return False
        self.sizes[b] += self.sizes[a]
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        matrix = [[0] * n for _ in range(m)]
        u = unionFind(m * n)

        def cal(i, j):
            return n * i + j

        ans = 0
        res = []
        visted = set()
        for r, c in positions:
            matrix[r][c] = 1
            num = cal(r, c)
            if num in visted:
                res.append(ans)
                continue
            visted.add(num)
            ans += 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 1:
                    nnum = cal(nr, nc)
                    if u.union(num, nnum):
                        ans -= 1
            res.append(ans)
        return res
