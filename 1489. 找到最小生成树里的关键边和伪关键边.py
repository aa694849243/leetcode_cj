# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi,
# weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权
# 值和最小。
#
#  请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在
# 某些最小生成树中但不会出现在所有最小生成树中的边。
#
#  请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。
#
#
#
#  示例 1：
#
#
#
#  输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# 输出：[[0,1],[2,3,4,5]]
# 解释：上图描述了给定图。
# 下图是所有的最小生成树。
#
# 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
# 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
#
#
#  示例 2 ：
#
#
#
#  输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# 输出：[[],[0,1,2,3]]
# 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。
#
#
#
#
#  提示：
#
#
#  2 <= n <= 100
#  1 <= edges.length <= min(200, n * (n - 1) / 2)
#  edges[i].length == 3
#  0 <= fromi < toi < n
#  1 <= weighti <= 1000
#  所有 (fromi, toi) 数对都是互不相同的。
#
#  Related Topics 并查集 图 最小生成树 排序 强连通分量 👍 113 👎 0

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
        if a == b:
            return False
        if self.sizes[a] < self.sizes[b]:
            self.sizes[a], self.sizes[b] = self.sizes[b], self.sizes[a]
        self.f[b] = a
        self.sizes[a] += self.sizes[b]
        self.vcount -= 1
        return True

    def connect(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        leng = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])
        u = unionFind(n)
        v = 0
        for i in range(leng):
            if u.union(edges[i][0], edges[i][1]):
                v += edges[i][2]
        ans = [[], []]
        for i in range(leng):
            uf = unionFind(n)
            vf = 0
            for j in range(leng):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    vf += edges[j][2]
            if uf.vcount != 1 or vf != v:
                ans[0].append(edges[i][3])
                continue
            uf = unionFind(n)
            uf.union(edges[i][0], edges[i][1])
            vf = edges[i][2]
            for k in range(leng):
                if i != k and uf.union(edges[k][0], edges[k][1]):
                    vf += edges[k][2]
            if vf == v:
                ans[1].append(edges[i][3])
        return ans


Solution().findCriticalAndPseudoCriticalEdges(6, [[0, 1, 1], [1, 2, 1], [0, 2, 1], [2, 3, 4], [3, 4, 2], [3, 5, 2],
                                                  [4, 5, 2]])
