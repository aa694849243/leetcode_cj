#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。
#
#  示例:
#
#  现有矩阵 matrix 如下：
#
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
#
#  给定 target = 5，返回 true。
#
#  给定 target = 20，返回 false。
#  Related Topics 数组 二分查找 分治 矩阵
#  👍 29 👎 0


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        R, C = len(matrix), len(matrix[0])

        def binsect(l, r, nums):
            while l < r:
                mid = (l + r) // 2
                if target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l

        l, r = 0, C
        row = R - 1
        while row >= 0:
            p = binsect(l, r, matrix[row])
            row -= 1
            if p == l:
                continue
            if matrix[row + 1][p - 1] == target:
                return True
            if p >= C:
                return False
            l = p
        return False


Solution().searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
