# -*- coding: utf-8 -*-
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, fa) -> int:  # -1为断开情况
            cur = nums[node]
            for nxt in g[node]:
                if nxt != fa:
                    res = dfs(nxt, node)
                    if res >= 0:
                        cur += res
                        if cur > target:
                            return -1
                    else:
                        return -1
            return 0 if cur == target else cur

        n = len(nums)
        total = sum(nums)
        for conn_num in range(total // max(nums), 1, -1):  # conn_num为连通块的个数,连通分量为1的话，删不了任何边
            if total % conn_num == 0:
                target = total // conn_num
                if dfs(0, -1) == 0:
                    return conn_num - 1
        return 0


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().componentValue(
    [1, 2, 1, 1, 1],
    [[0, 1], [1, 3], [3, 4], [4, 2]]
))
