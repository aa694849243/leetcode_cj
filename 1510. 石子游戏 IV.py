#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(None)
        def rec(n):
            if int(n ** 0.5) ** 2 == n:
                return True
            for i in range(1,int(n**.5)+1):
                if not rec(n-i**2):
                    return True
            return False
        return rec(n)