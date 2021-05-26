# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
#
#  如果不能形成任何面积不为零的三角形，返回 0。
#
#
#
#
#
#
#  示例 1：
#
#  输入：[2,1,2]
# 输出：5
#
#
#  示例 2：
#
#  输入：[1,2,1]
# 输出：0
#
#
#  示例 3：
#
#  输入：[3,2,3,4]
# 输出：10
#
#
#  示例 4：
#
#  输入：[3,6,2,3]
# 输出：8
#
#
#
#
#  提示：
#
#
#  3 <= A.length <= 10000
#  1 <= A[i] <= 10^6
#
#  Related Topics 排序 数学
#  👍 140 👎 0


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def judge(a, b, c):
            if a + b <= c:
                return False
            return True

        nums.sort()
        n = len(nums)
        l, m, r = n - 3, n - 2, n - 1
        while l >= 0:
            if judge(nums[l], nums[m], nums[r]):
                return nums[l] + nums[m] + nums[r]
            else:
                l -= 1
                m -= 1
                r -= 1
        return 0
