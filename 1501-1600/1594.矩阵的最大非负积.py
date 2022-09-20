import math
from typing import List


# @solution-sync:begin
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        res=float('inf')
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    res = 0
        dp = grid[0].copy()
        for i in range(1, C):
            dp[i] = grid[0][i] * dp[i - 1]
        dp = [[dp[i] if dp[i] >= 0 else float('inf'), dp[i] if dp[i] < 0 else float('-inf')] for i in range(C)]
        for r in range(1, R):
            tmp_dp = dp.copy()
            for c in range(C):
                if c == 0:
                    a, b = grid[r][c] * dp[0][0], grid[r][c] * dp[0][1]
                    a, b = max(a, b), min(a, b)
                    tmp_dp[c][0] = a if a >= 0 else float('inf')
                    tmp_dp[c][1] = b if b < 0 else float('-inf')
                else:
                    left_a, left_b = grid[r][c] * tmp_dp[c - 1][0], grid[r][c] * tmp_dp[c - 1][1]
                    up_a, up_b = grid[r][c] * dp[c][0], grid[r][c] * dp[c][1]
                    li = [x for x in [left_a, left_b, up_a, up_b] if x not in (float('inf'), float('-inf')) and not math.isnan(x)]
                    a = max(li) if li else float('inf')
                    b = min(li) if li else float('-inf')
                    tmp_dp[c][0] = a if a >= 0 else float('inf')
                    tmp_dp[c][1] = b if b < 0 else float('-inf')
            dp = tmp_dp
        res = dp[-1][0] if dp[-1][0]<float('inf') else res
        return res % mod if res < float('inf') else -1


Solution().maxProductPath([[-1, 3, 0], [3, -2, 3], [-1, 1, -4]])
