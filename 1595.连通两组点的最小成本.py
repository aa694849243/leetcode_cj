from functools import lru_cache
from typing import List


# @solution-sync:begin
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # @solution-begin:begin
        m, n = len(cost), len(cost[0])
        min_j = [min(cost[i][j] for i in range(m)) for j in range(n)]

        @lru_cache(None)
        def dp(i, used):
            if i == m:
                res = 0
                for j in range(n):
                    if used & (1 << j) == 0:
                        res += min_j[j]
                return res
            res = float('inf')
            for j in range(n):
                res = min(res, dp(i + 1, used | (1 << j)) + cost[i][j])
            return res

        return dp(0, 0)
