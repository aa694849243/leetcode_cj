#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import heapq
from typing import List


# 村里面一共有 n 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。
#
#  对于每个房子 i，我们有两种可选的供水方案：
#
#
#  一种是直接在房子内建造水井，成本为 wells[i]；
#  另一种是从另一口井铺设管道引水，数组 pipes 给出了在房子间铺设管道的成本，其中每个 pipes[i] = [house1, house2, cost
# ] 代表用管道将 house1 和 house2 连接在一起的成本。当然，连接是双向的。
#
#
#  请你帮忙计算为所有房子都供水的最低总成本。
#
#
#
#  示例 1：
#
#
#
#
# 输入：n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# 输出：3
# 解释：
# 上图展示了铺设管道连接房屋的成本。
# 最好的策略是在第一个房子里建造水井（成本为 1），然后将其他房子铺设管道连起来（成本为 2），所以总成本为 3。
#
#
#  示例 2：
#
#
# 输入：n = 2, wells = [1,1], pipes = [[1,2,1]]
# 输出：2
#
#
#
#  提示：
#
#
#  1 <= n <= 10000
#  wells.length == n
#  0 <= wells[i] <= 10^5
#  1 <= pipes.length <= 10000
#  1 <= pipes[i][0], pipes[i][1] <= n
#  0 <= pipes[i][2] <= 10^5
#  pipes[i][0] != pipes[i][1]
#
#  Related Topics 并查集 图 最小生成树
#  👍 59 👎 0

# prim算法
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = pipes
        for i, c in enumerate(wells):
            edges.append([0, i + 1, c])
        g = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        for vi, vj, cost in edges:
            g[vi][vj] = min(g[vi][vj], cost)
            g[vj][vi] = min(g[vj][vi], cost)
        res = 0
        pq = []
        visted = set()
        heapq.heappush(pq, (0, 0))
        while pq and len(visted) < n + 1:
            cost, v = heapq.heappop(pq)
            if v in visted:
                continue
            visted.add(v)
            res += cost
            for nxt, c in g[v].items():
                heapq.heappush(pq, (c, nxt))
        return res


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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = pipes
        for i, c in enumerate(wells):
            edges.append([0, i + 1, c])
        edges.sort(key=lambda x: x[2])
        u = unionfind(n + 1)
        res = 0
        for a, b, c in edges:
            if u.connect(a, b):
                continue
            u.union(a, b)
            res += c
            if u.part == 1:
                break
        return res