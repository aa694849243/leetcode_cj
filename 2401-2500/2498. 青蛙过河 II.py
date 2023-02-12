# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-28 4:03 
# ide： PyCharm
import bisect
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)

        def check(dis):
            p = 0
            vis = [0] * n
            while 1:
                nxt = stones[p] + dis
                nxt_p = bisect.bisect_right(stones, nxt)
                if nxt_p - p <= 1:
                    return False
                p = nxt_p - 1
                vis[p] = 1
                if p == n - 1:
                    break
            p = n - 2
            cur = stones[n - 1]
            while p >= 0:
                if vis[p]:
                    p -= 1
                    continue
                if cur - stones[p] > dis:
                    return False
                cur = stones[p]
                p -= 1
            return True

        l, r = 0, 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().maxJump([0, 2, 5, 6, 7])
)
