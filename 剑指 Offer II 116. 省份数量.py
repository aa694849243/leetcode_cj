# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 23:17 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind()
        res = n
        for i in range(n):
            for j in range(i):
                if isConnected[i][j] and not uf.connect(i, j):
                    uf.union(i, j)
                    res -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)

