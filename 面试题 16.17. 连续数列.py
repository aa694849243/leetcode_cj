#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一个整数数组，找出总和最大的连续数列，并返回总和。
#
#  示例：
#
#  输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
#  进阶：
#
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#  Related Topics 数组 分治 动态规划
#  👍 87 👎 0

# 1线段树
class Stree:
    def __init__(self, lsum, rsum, isum, msum):
        self.lsum = lsum
        self.rsum = rsum
        self.isum = isum
        self.msum = msum

    def get(self, nums, l, r):
        if l == r:
            return Stree(nums[l], nums[l], nums[l], nums[l])
        mid = (l + r) >> 1
        L = self.get(nums, l, mid)
        R = self.get(nums, mid + 1, r)
        return self.pushup(L, R)

    def pushup(self, L, R):
        isum = L.isum + R.isum
        lsum = max(L.lsum, L.isum + R.lsum)
        rsum = max(R.rsum, R.isum + L.rsum)
        msum = max(max(L.msum, R.msum), L.rsum + R.lsum)
        return Stree(lsum, rsum, isum, msum)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = Stree(0, 0, 0, 0).get(nums, 0, len(nums) - 1).msum
        return s
