#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 有一队人（两人或以上）想要在一个地方碰面，他们希望能够最小化他们的总行走距离。
#
#  给你一个 2D 网格，其中各个格子内的值要么是 0，要么是 1。
#
#  1 表示某个人的家所处的位置。这里，我们将使用 曼哈顿距离 来计算，其中 distance(p1, p2) = |p2.x - p1.x| + |p2.y
#  - p1.y|。
#
#  示例：
#
#  输入:
#
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# 输出: 6
#
# 解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
#      (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。
#  Related Topics 数组 数学 矩阵 排序
#  👍 80 👎 0


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rs, cs = [], []
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    rs.append(r)
                    cs.append(c)
        rs.sort()
        cs.sort()
        rmid = rs[len(rs) // 2]
        cmid = cs[len(cs) // 2]
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    res += abs(r - rmid) + abs(c - cmid)
        return res
Solution().minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])