#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax2 + bx + c，请将函数值产生
# 的数组返回。
#
#  要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。
#
#  示例 1：
#
#  输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# 输出: [3,9,15,33]
#
#
#  示例 2：
#
#  输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# 输出: [-23,-5,1,7]
#
#  Related Topics 数组 数学 双指针 排序
#  👍 53 👎 0


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(num):
            return a * num ** 2 + b * num + c

        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        if a >= 0:
            idx = r
            while l <= r:
                y1, y2 = f(nums[l]), f(nums[r])
                if y1 > y2:
                    res[idx] = y1
                    l += 1
                else:
                    res[idx] = y2
                    r -= 1
                idx -= 1
        else:
            idx = 0
            while l <= r:
                y1, y2 = f(nums[l]), f(nums[r])
                if y1 < y2:
                    res[idx] = y1
                    l += 1
                else:
                    res[idx] = y2
                    r -= 1
                idx -= 1
        return res
