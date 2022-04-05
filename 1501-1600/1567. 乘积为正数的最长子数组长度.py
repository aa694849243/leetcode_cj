#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
#
#  一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
#
#  请你返回乘积为正数的最长子数组长度。
#
#
#
#  示例 1：
#
#  输入：nums = [1,-2,-3,4]
# 输出：4
# 解释：数组本身乘积就是正数，值为 24 。
#
#
#  示例 2：
#
#  输入：nums = [0,1,-2,-3,-4]
# 输出：3
# 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
# 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
#
#  示例 3：
#
#  输入：nums = [-1,-2,-3,0,1]
# 输出：2
# 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
#
#
#  示例 4：
#
#  输入：nums = [-1,2]
# 输出：1
#
#
#  示例 5：
#
#  输入：nums = [1,2,3,5,-6,4,0,10]
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  -10^9 <= nums[i] <= 10^9
#
#  Related Topics 贪心 数组 动态规划
#  👍 98 👎 0


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        neg = -1
        pos = -1
        res = 0
        cur = 1
        for i, num in enumerate(nums):
            cur *= num
            if cur < 0:
                if neg != -1:
                    res = max(res, i - neg)
                else:
                    neg = i
            elif cur > 0:
                res = max(i - pos, res)
            else:  # cur=0
                neg, pos = -1, i
                cur = 1
        return res


Solution().getMaxLen([-1, -2, -3, 0, 1])
