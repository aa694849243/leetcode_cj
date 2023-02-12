# -*- coding: utf-8 -*-
# datetime： 2023-02-01 23:47
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        # 前两个操作不会改变gcd(x,y)
        x = math.gcd(targetX, targetY)
        return x & (x - 1) == 0
# leetcode submit region end(Prohibit modification and deletion)

