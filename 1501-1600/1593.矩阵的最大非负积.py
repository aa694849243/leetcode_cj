from typing import List


# @solution-sync:begin
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        R, C = len(grid), len(grid[0])
        dp = grid[0]
        for i in range(1, C):
            dp[i] *= dp[i - 1]
        ma=float('-inf')
        for r in range(1, R):
            for c in range(C):
                if c == 0:
                    dp[c] *= grid[r][c]
