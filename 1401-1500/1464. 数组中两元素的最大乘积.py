# -*- coding: utf-8 -*-

# 给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。
#
#  请你计算并返回该式的最大值。
#
#
#
#  示例 1：
#
#  输入：nums = [3,4,5,2]
# 输出：12
# 解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) =
#  3*4 = 12 。
#
#
#  示例 2：
#
#  输入：nums = [1,5,4,5]
# 输出：16
# 解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
#
#
#  示例 3：
#
#  输入：nums = [3,7]
# 输出：12
#
#
#
#
#  提示：
#
#
#  2 <= nums.length <= 500
#  1 <= nums[i] <= 10^3
#
#  Related Topics 数组 排序 堆（优先队列） 👍 24 👎 0


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lst = [float('-inf'), float('-inf')]
        for num in nums:
            if num > lst[0]:
                lst[0] = num
                if num > lst[1]:
                    lst[0], lst[1] = lst[1], lst[0]
        return (lst[0]-1)*(lst[1]-1)