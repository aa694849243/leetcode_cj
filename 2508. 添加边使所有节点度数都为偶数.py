# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-29 23:02 
# ide： PyCharm
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g = collections.defaultdict(set)
        degrees = [0] * (n + 1)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            degrees[u] += 1
            degrees[v] += 1
        odd = []
        for i, d in enumerate(degrees):
            if d % 2 == 1:
                odd.append(i)
        if len(odd) == 0:
            return True
        if len(odd) == 2:
            a, b = odd
            if a not in g[b]:
                return True
            for i in range(1, n + 1):
                if i not in g[a] and i not in g[b] and i not in (a, b):
                    return True
        if len(odd) == 4:
            a, b, c, d = odd
            if a not in g[b] and c not in g[d] or a not in g[c] and b not in g[d] or a not in g[d] and b not in g[c]:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)

