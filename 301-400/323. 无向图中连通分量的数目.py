# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。
#
#  示例 1:
#
#  输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# 输出: 2
#
#
#  示例 2:
#
#  输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# 输出:  1
#
#
#  注意:
# 你可以假设在 edges 中不会出现重复的边。而且由于所以的边都是无向边，[0, 1] 与 [1, 0] 相同，所以它们不会同时在 edges 中出现。
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 118 👎 0
class unionFind:
    def __init__(self, n):
        self.f = {}
        self.vcount = n
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
            self.vcount -= 1
            self.f[b] = a


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for vi, vj in edges:
            g[vi].append(vj)
            g[vj].append(vi)
        visted = set()
        u = unionFind(n)

        def dfs(node):
            for nxt in g[node]:
                if nxt not in visted:
                    visted.add(nxt)
                    u.union(u, nxt)
                    dfs(nxt)

        for i in range(n):
            if i not in visted:
                visted.add(i)
                dfs(i)
        return u.vcount
Solution().countComponents(5, [[0,1],[1,2],[3,4]])