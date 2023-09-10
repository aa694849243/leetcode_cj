# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-05-08 1:16 
# ide： PyCharm
import bisect


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        l = bisect.bisect_right(nums, 0)
        x_minus = nums[:l]
        x_plus = nums[l:]
        res = len(x_plus)
        prefix=sum(x_plus)
        for num in x_minus[::-1]:
            prefix += num
            if prefix > 0:
                res += 1
            else:
                break
        return res

# leetcode submit region end(Prohibit modification and deletion)
