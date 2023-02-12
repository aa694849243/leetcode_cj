# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-30 22:41 
# ide： PyCharm
import bisect

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)

        def check(x):
            p = 0
            cnt = 1
            while 1:
                nxt = bisect.bisect_left(price, price[p] + x)
                if nxt >= len(price):
                    break
                p = nxt
                cnt += 1
            return cnt >= k

        l, r = 1, 10 ** 9
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l if check(l) else l - 1


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().maximumTastiness([13, 5, 1, 8, 21, 2], 3)
)

