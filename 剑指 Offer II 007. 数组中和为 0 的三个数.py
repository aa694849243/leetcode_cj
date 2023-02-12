# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-05 1:14 
# ide： PyCharm
import bisect

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if num + nums[l] + nums[r] == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res

