#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 5966. 还原原数组
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        li = sorted(nums)
        if len(li) == 2:
            if (li[1] - li[0]) % 2 == 0:
                return [li[0]+(li[1] - li[0]) // 2]

        def judge(lst, k):
            lst = collections.deque(lst)
            C = collections.Counter(lst)
            arr = []
            while lst:
                a = lst.popleft()
                if C[a] > 0:
                    C[a] -= 1
                    if C[a + 2 * k] > 0:
                        C[a + 2 * k] -= 1
                        arr.append(a + k)
                    else:
                        return []
                else:
                    continue
            return arr

        for i in range(1, len(nums) // 2+1):
            k = (li[i] - li[0])
            if k!=0 and k % 2 == 0:
                arr = judge(li[:], k // 2)
                if arr:
                    return arr


Solution().recoverArray([1,1,3,3])
