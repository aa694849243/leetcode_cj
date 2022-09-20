import collections
from typing import List


# @solution-sync:begin
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        m = collections.defaultdict(int)
        g = collections.defaultdict(set)
        for vi, vj in roads:
            g[vi].add(vj)
            g[vj].add(vi)
            m[vi] += 1
            m[vj] += 1
        res = 0
        for vi in range(n):
            for vj in range(vi + 1, n):
                if vj in g[vi]:
                    res = max(res, m[vi] + m[vj] - 1)
                else:
                    res=max(res, m[vi] + m[vj])
        return res
# @solution-sync:end
