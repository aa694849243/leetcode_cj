#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bisect
import collections

# 5952. 环和杆
import itertools


class Solution:
    def countPoints(self, rings: str) -> int:
        A, B = rings[::2], rings[1::2]
        m = collections.defaultdict(int)
        res = 0
        for a, b in zip(A, B):
            if a == 'R':
                m[b] |= 1
            elif a == 'G':
                m[b] |= (1 << 1)
            else:
                m[b] |= (1 << 2)
        for k in m:
            if m[k] == 7:
                res += 1
        return res


# 5953. 子数组范围和
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 1):
            mi, ma = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                mi = min(nums[j], mi)
                ma = max(nums[j], ma)
                res += ma - mi
        return res


# 5954. 给植物浇水 II
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a, b = capacityA, capacityB
        l, r = 0, len(plants) - 1
        cnt = 0
        while l <= r:
            if l < r:
                if a >= plants[l]:
                    a -= plants[l]
                else:
                    a = capacityA - plants[l]
                    cnt += 1
                if b >= plants[r]:
                    b -= plants[r]
                else:
                    b = capacityB - plants[r]
                    cnt += 1
                l += 1
                r -= 1
            else:
                if max(a, b) < plants[l]:
                    cnt += 1
                l += 1
                r -= 1
        return cnt


# 5955. 摘水果
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        m = collections.defaultdict(int)
        for i, j in fruits:
            m[i] = j

        li = [0] + [*itertools.accumulate(m.values())]
        index = bisect.bisect_left(fruits, [startPos, float('inf')])
        if index == 0:
            rindex = bisect.bisect_left(fruits, [startPos + k, float('inf')])
            if rindex == 0:
                return 0
            else:
                return li[rindex]
        res = 0
        for i in range(index):
            l = fruits[i][0]
            if startPos - l <= k:
                k1 = k - 2 * (startPos - l)
                k2 = (k - (startPos - l)) // 2
                if k1 > k2 and k1 > 0:
                    rindex = bisect.bisect_left(fruits, [startPos + k1, float('inf')])
                elif k2 > k1 and k2 > 0:
                    rindex = bisect.bisect_left(fruits, [startPos + k2, float('inf')])
                else:
                    rindex = bisect.bisect_left(fruits, [startPos, float('inf')])
                res = max(li[rindex] - li[i], res)
        rindex = bisect.bisect_left(fruits, [startPos + k, float('inf')])
        l = index
        res = max(li[rindex] - li[l], res)
        return res


Solution().maxTotalFruits([[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], 5, 4)
