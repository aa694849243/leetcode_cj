#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        p = collections.deque()
        pnt = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pnt += 1
                p.append(0)
                while pnt > 1:
                    a = p.popleft()
                    if a == 0:
                        pnt -= 1
            else:
                p.append(1)
            res = max(len(p)-1, res)
        return res
Solution().longestSubarray([1,1,1])