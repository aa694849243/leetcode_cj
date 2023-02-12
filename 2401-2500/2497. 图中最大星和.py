# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-28 3:18 
# ide： PyCharm
import collections
from typing import List
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
from math import inf
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g = collections.defaultdict(list)
        for u, v in edges:
            heapq.heappush(g[u], -vals[v])
            heapq.heappush(g[v], -vals[u])
        ans = -inf
        for i in range(len(vals)):
            cnt = 0
            tmp = vals[i]
            while g[i] and g[i][0] < 0 and cnt < k:
                tmp += -heapq.heappop(g[i])
                cnt += 1
            ans = max(ans, tmp)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().maxStarSum(
        [1, 2, 3, 4, 10, -10, -20],
        [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]],
        2
    ))
