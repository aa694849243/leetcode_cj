# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长连续子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。
#
#
#
#  示例 1:
#
#
# 输入: nums = [1,-1,5,-2,3], k = 3
# 输出: 4
# 解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
#
#
#  示例 2:
#
#
# 输入: nums = [-2,-1,2,1], k = 1
# 输出: 2
# 解释: 子数组 [-1, 2] 和等于 1，且长度最长。
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#  -10⁹ <= k <= 10⁹
#
#  Related Topics 数组 哈希表 👍 142 👎 0


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixcum = [0] + [*itertools.accumulate(nums)]
        m = {}
        m[0] = 0
        res = 0
        for i, num in enumerate(prefixcum[1:], 1):
            target = num-k
            if target in m:
                res = max(res, i - m[target])
            m.setdefault(num, i)
        return res


Solution().maxSubArrayLen([-2, -1, 2, 1], 1)
