# -*- coding: utf-8 -*-
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod=10**9+7
        R, C = len(grid), len(grid[0])
        m = collections.defaultdict(lambda: collections.defaultdict(int))
        visted = set()

        def dp(r, c, cur):
            visted.add((r, c))
            if r == 0 and c == 0:
                m[r, c][grid[r][c] % k] = 1
                return
            cur_k = (cur - grid[r][c]) % k
            r1, c1 = r - 1, c
            if r1 >= 0 and c1 >= 0:
                if (r1, c1) not in visted:
                    dp(r1, c1, cur_k)
                m[r, c][cur] += m[r1, c1][cur_k]
            r2, c2 = r, c - 1
            if r2 >= 0 and c2 >= 0:
                if (r2,c2) not in visted:
                    dp(r2, c2, cur_k)
                m[r, c][cur] += m[r2, c2][cur_k]
            return
        dp(R - 1, C - 1, 0)
        return m[R - 1, C - 1][0]%mod