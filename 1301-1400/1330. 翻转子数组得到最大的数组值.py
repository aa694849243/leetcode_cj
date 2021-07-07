# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。
#
#  你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。
#
#  请你找到可行的最大 数组值 。
#
#
#
#  示例 1：
#
#  输入：nums = [2,3,1,5,4]
# 输出：10
# 解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
#
#
#  示例 2：
#
#  输入：nums = [2,4,9,24,2,1,10]
# 输出：68
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 3*10^4
#  -10^5 <= nums[i] <= 10^5
#
#  Related Topics 贪心 数组 数学
#  👍 48 👎 0


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        na=sum(abs(nums[i]-nums[i-1]) for i in range(1,n))
        a = max(min(nums[i], nums[i - 1]) for i in range(1, n))  # 最高负位值
        b = min(max(nums[i], nums[i - 1]) for i in range(1, n))  # 最低正位值
        d=0
        for i in range(1,n): #考虑端点
            d=max(abs(nums[i]-nums[0])-abs(nums[i]-nums[i-1]),d) #左端点
            d=max(abs(nums[-1]-nums[i-1])-abs(nums[i]-nums[i-1]),d)
        return na+max(2*a-2*b,d)


