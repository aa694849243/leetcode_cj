# -*- coding: utf-8 -*-
# !/usr/bin/env python
from typing import List


# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2
# ] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
#
#  示例 1：
#
#  输入：[3,4,5,1,2]
# 输出：1
#
#
#  示例 2：
#
#  输入：[2,2,2,0,1]
# 输出：0
#
#
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sor
# ted-array-ii/
#  Related Topics 数组 二分查找
#  👍 356 👎 0

# 为什么不能用left和mid比，因为题解给的算法是一个类似计算下坡的算法，如果出现纯上坡的数组或者诸如nums[left]==nums[mid]的情况会一步步将left移动到谷底，也形成了一个纯上坡的数组，用一个计算下坡中某值在哪里的算法去上坡数组里找，当然找不到
# 为什么选左边中位数：当只剩下两个数的时候，我如果取右中位数就是自己和自己比较了，而不是两个数比较。
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1
        while l < r:  # 小于和小于等于都可以
            mid = (l + r) // 2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid + 1
            else:
                r -= 1
        return numbers[l]


Solution().minArray([3, 1, 3, 3])
