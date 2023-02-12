# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 23:30 
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

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind()
        m = {}
        strs = list(set(strs))

        def check(s1, s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt == 2 or cnt == 0

        ans = len(strs)
        for s in strs:
            kv = ''.join(sorted(s))
            if kv not in m:
                m[kv] = [s]
            else:
                for s2 in m[kv]:
                    if check(s, s2) and not uf.is_connected(s, s2):
                        uf.union(s, s2)
                        ans -= 1
                m[kv].append(s)
        return ans

# leetcode submit region end(Prohibit modification and deletion)

