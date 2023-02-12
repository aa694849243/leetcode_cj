# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 23:38 
# ide： PyCharm
class UnionFind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        self.f[self.find(y)] = self.find(x)

    def connect(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        res = None
        for u, v in edges:
            if uf.connect(u, v):
                res = [u, v]
            uf.union(u, v)
        return res
# leetcode submit region end(Prohibit modification and deletion)

