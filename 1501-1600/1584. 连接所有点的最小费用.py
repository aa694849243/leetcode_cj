#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import heapq
from typing import List


# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
#
#  连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示
# val 的绝对值。
#
#  请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
#
#
#
#  示例 1：
#
#
#
#
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
#
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
#
#
#  示例 2：
#
#
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
#
#
#  示例 3：
#
#
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
#
#
#  示例 4：
#
#
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
#
#
#  示例 5：
#
#
# 输入：points = [[0,0]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= points.length <= 1000
#  -106 <= xi, yi <= 106
#  所有点 (xi, yi) 两两不同。
#
#  Related Topics 并查集 数组 最小生成树
#  👍 181 👎 0

class unionfind:
    def __init__(self, n):
        self.part = n
        self.size = collections.defaultdict(lambda: 1)
        self.f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.f[b] = a
            self.size[a] += self.size[b]
            self.part -= 1

    def connect(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cal(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        n = len(points)
        uf = unionfind(n)
        ans = 0
        pq = []
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(pq, [cal(points[i], points[j]), i, j])
        while uf.part != 1:
            dis, i, j = heapq.heappop(pq)
            if uf.connect(i, j):
                continue
            else:
                ans += dis
                uf.union(i, j)
        return ans
