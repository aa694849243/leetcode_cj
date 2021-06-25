# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
#
#
#
#
#
#
#  示例 1：
#
#  输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
#
#  示例 2：
#
#  输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
#
#
#  示例 3：
#
#  输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 4 * 10^4
#  1 <= nums[i] <= 10^4
#
#  Related Topics 动态规划
#  👍 129 👎 0


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a = [0, 0, 0]
        for num in nums:
            na0 = num + a[0]
            na1 = num + a[1]
            na2 = num + a[2]
            a[na0 % 3] = max(na0, a[na0 % 3])
            a[na1 % 3] = max(na1, a[na1 % 3])
            a[na2 % 3] = max(na2, a[na2 % 3])
        return a[0]
Solution().maxSumDivThree([1,2,3,4,4])