# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-05 23:23 
# ide： PyCharm
import bisect
import itertools


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        precum = [0] + [*itertools.accumulate(nums)]
        ans = math.inf
        for i in range(1, len(precum)):
            if precum[i] >= target:
                left = bisect.bisect_right(precum, precum[i] - target, 0, i)
                ans = min(ans, i - left + 1)
        return ans if ans != math.inf else 0
# leetcode submit region end(Prohibit modification and deletion)

