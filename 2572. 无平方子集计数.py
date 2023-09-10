# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-20 21:48 
# ide： PyCharm
import collections
import copy

# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedList

prims = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
mod = 10 ** 9 + 7
m = {
    1: 0,
    2: (1 << 0),
    3: (1 << 1),
    5: (1 << 2),
    6: (1 << 0) | (1 << 1),
    7: (1 << 3),
    10: (1 << 0) | (1 << 2),
    11: (1 << 4),
    13: (1 << 5),
    14: (1 << 0) | (1 << 3),
    15: (1 << 1) | (1 << 2),
    17: (1 << 6),
    19: (1 << 7),
    21: (1 << 1) | (1 << 3),
    22: (1 << 0) | (1 << 4),
    23: (1 << 8),
    26: (1 << 0) | (1 << 5),
    29: (1 << 9),
    30: (1 << 0) | (1 << 1) | (1 << 2)
}

from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        ans = 0
        c = collections.defaultdict(int)
        lst = []
        for num in nums:
            if num in m:
                lst.append(m[num])
        for i, num in enumerate(lst):
            tmp = collections.defaultdict(int)
            for k, v in c.items():
                if k & num == 0:
                    tmp[k | num] += v
                    ans += v
            tmp[num] += 1
            ans += 1
            ans %= mod
            for k, v in c.items():
                tmp[k] += v
            c = tmp
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().squareFreeSubsets(
        [17,27,20,1,19]
    )
)

