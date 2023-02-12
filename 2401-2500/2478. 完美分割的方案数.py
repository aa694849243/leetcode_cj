# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-27 2:07 
# ide： PyCharm
from functools import lru_cache


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        f = [[0] * k for _ in range(len(s))]
        if k * minLength > len(s) or s[0] not in '2357' or s[-1] in '2357':
            return 0
        mod = 10 ** 9 + 7
        ids = [0]
        for i in range(1, len(s)):
            if s[i] in '2357' and s[i - 1] not in '2357':
                ids.append(i)

        @lru_cache(None)
        def f(p, k):
            if k == 1:
                return 1
            ans = 0
            for i in range(p + 1, len(ids)):
                idx = ids[i]
                if idx - ids[p] >= minLength and (len(s) - idx) // (k - 1) >= minLength and len(ids[i:]) >= k - 1:
                    ans += f(i, k - 1)
                    ans %= mod
            return ans

        return f(0, k)

