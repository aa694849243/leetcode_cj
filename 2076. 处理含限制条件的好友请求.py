# -*- coding: utf-8 -*-
class unionfind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.f[b] = a


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = unionfind()
        res = []
        for x, y in requests:
            a, b = uf.find(x), uf.find(y)
            if a == b:
                res.append(True)
            else:
                for u,v in restrictions:
                    tmp_u,tmp_v = uf.find(u),uf.find(v)
                    if sorted([tmp_u,tmp_v]) == sorted([a,b]):
                        res.append(False)
                        break
                else:
                    uf.union(a,b)
                    res.append(True)
        return res
