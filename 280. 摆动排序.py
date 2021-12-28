#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。
#
#  示例:
#
#  输入: nums = [3,5,2,1,6,4]
# 输出: 一个可能的解答是 [3,5,1,6,2,4]
#  Related Topics 贪心 数组 排序
#  👍 82 👎 0

# 一个显而易见的解法是先将数组排序，再从第二个元素开始逐对交换元素的位置。如：+=2
# 摆动排序
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 1
        i, j = 0, 1
        while j < len(nums):
            if flag == 1:
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
            flag *= -1
            i += 1
            j += 1
