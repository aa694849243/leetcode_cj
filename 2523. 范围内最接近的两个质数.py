# -*- coding: utf-8 -*-
# datetime： 2023-01-31 0:04
# ide： PyCharm
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isprim = [1] * (right + 1)
        isprim[0] = isprim[1] = 0
        for i in range(2, int(right ** 0.5) + 1):
            if isprim[i]:
                isprim[i ** 2:right + 1:i] = [0] * len(isprim[i ** 2:right + 1:i])
        ans = [-1, -1]
        mx = math.inf
        p1 = p2 = -1
        for i in range(left, right + 1):
            if isprim[i]:
                if p2 == -1:
                    p2 = i
                else:
                    p1, p2 = p2, i
                    if p2 - p1 < mx:
                        ans = [p1, p2]
                        mx = p2 - p1
        return ans

# leetcode submit region end(Prohibit modification and deletion)

