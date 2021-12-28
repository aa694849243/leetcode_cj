#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5963. 反转两次的数字
import collections
import itertools


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        return True


# 5964. 执行所有后缀指令
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dirs = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
        # R = [0]
        # C = [0]
        # for ch in s:
        #     dr, dc = dirs[ch]
        #     R.append(R[-1] + dr)
        #     C.append(C[-1] + dc)
        res = [0] * (leng := len(s))
        for i in range(leng):
            r, c = startPos
            for j in range(i, leng):
                dr, dc = dirs[s[j]]
                nr, nc = r + dr, c + dc
                r, c = nr, nc
                if 0 <= nr < n and 0 <= nc < n:
                    res[i] += 1
                else:
                    break
        return res


# 5965. 相同元素的间隔之和
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        m = collections.defaultdict(list)
        for i, num in enumerate(arr):
            m[num].append(i)
        res = [0] * len(arr)
        for num in m:
            presum = [0] + [*itertools.accumulate(m[num])]
            tn = len(m[num])
            for j, i in enumerate(m[num]):
                res[i] = (i * (j + 1) - presum[j + 1]) + (presum[-1] - presum[j + 1] - i * (tn - j - 1))
        return res

Solution().getDistances([2,1,3,1,2,3,3])