# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List
import bisect


# 5763. 哪种连续子字符串更长
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        o = 0
        l = 0
        lm = 0
        om = 0
        for i, val in enumerate(s):
            if i == 0:
                if val == '1':
                    l += 1
                else:
                    o += 1
            else:
                if val == s[i - 1]:
                    if val == '0':
                        o += 1
                    else:
                        l += 1
                else:
                    if val == '0':
                        lm = max(lm, l)
                        l = 0
                        o = 1
                    else:
                        om = max(om, o)
                        o = 0
                        l = 1
        if s[i] == '1':
            lm = max(l, lm)
        else:
            om = max(o, om)
        return lm > om


# 5764. 准时到达的列车最小时速
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def cal(h):
            s = 0
            for i in dist[:-1]:
                a = i / h
                if int(a) < a:
                    s += int(a) + 1
                else:
                    s += int(a)
            s += dist[-1] / h
            return s <= hour

        if len(dist) - 1 > hour:
            return -1
        l, r = 1, 10000001
        while l < r:
            mid = (l + r) // 2
            if not cal(mid):
                l = mid + 1
            else:
                r = mid
        return l if cal(l) else -1


# 5765. 跳跃游戏 VII
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        dp = [0] * len(s)
        dp[0] = 1
        n = len(s)
        flag = 0
        for i, val in enumerate(s):
            if val == '0' and dp[i] == 1:
                if i == 0:
                    for nxt in range(minJump, maxJump + 1):
                        if nxt >= n:
                            break
                        if s[nxt] == '0':
                            dp[nxt] = 1
                    l = minJump
                    r = nxt
                else:
                    gap = i - flag
                    for nxt in range(max(r + 1, i + minJump), min(r + gap + 1, i + maxJump + 1)):
                        if nxt >= n:
                            break
                        if s[nxt] == '0':
                            dp[nxt] = 1

                    r = nxt
        return dp[-1] == 1


# 5766. 石子游戏 VIII
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        cum = [0] + [*itertools.accumulate(stones)]
        m = {}
        j = len(stones)

        def dp(i):
            if i == j-1:
                return cum[j]
            if i in m:
                return m[i]
            m[i] = max(cum[i + 1] - dp(i + 1), dp(i + 1)) #cum[i+1]代表前i项累加和
            return m[i]

        return dp(1)


Solution().stoneGameVIII([25, -36, -32])
