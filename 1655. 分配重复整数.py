import collections, heapq, itertools
import functools
from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = collections.Counter(nums)
        resource = list(c.values())
        length = len(quantity)
        target = (1 << length) - 1

        @functools.lru_cache(None)
        def f(i, status, t):
            if status == target:
                return True
            if i == len(resource):
                return False
            lim = resource[i]
            for j in range(len(quantity)):
                if status & (1 << j) == 0 and t + quantity[j] <= lim:
                    if f(i, status | (1 << j), t + quantity[j]):
                        return True
            return f(i + 1, status, 0)
        return f(0, 0, 0)


a = Solution().canDistribute([1, 1, 2, 2], [2, 2])
print(a)
