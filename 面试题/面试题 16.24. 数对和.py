#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
#
#  示例 1:
#
#  输入: nums = [5,6,5], target = 11
# 输出: [[5,6]]
#
#  示例 2:
#
#  输入: nums = [5,6,5,6], target = 11
# 输出: [[5,6],[5,6]]
#
#  提示：
#
#
#  nums.length <= 100000
#
#  Related Topics 数组 哈希表 双指针 计数 排序
#  👍 29 👎 0


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = []
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
        return res
