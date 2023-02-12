# -*- coding: utf-8 -*-
# datetime： 2023-01-30 17:55
# ide： PyCharm
import math


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/solution/er-fen-da-an-by-endlesscheng-y8fp/
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = math.lcm(divisor1, divisor2)

        def check(x):
            share = x - x // divisor1 - x // divisor2 + x // lcm
            d1_share = max(uniqueCnt1 - x // divisor2 + x // lcm, 0)
            d2_share = max(uniqueCnt2 - x // divisor1 + x // lcm, 0)
            return share >= d1_share + d2_share

        l, r = 1, (uniqueCnt1 + uniqueCnt2) * 2 - 1  # 最坏情况d1=d2=2
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimizeSet(2, 7, 1, 3))

