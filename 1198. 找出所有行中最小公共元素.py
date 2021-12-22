# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个矩阵 mat，其中每一行的元素都已经按 严格递增 顺序排好了。请你帮忙找出在所有这些行中 最小的公共元素。
#
#  如果矩阵中没有这样的公共元素，就请返回 -1。
#
#
#
#  示例：
#
#
# 输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= mat.length, mat[i].length <= 500
#  1 <= mat[i][j] <= 10^4
#  mat[i] 已按严格递增顺序排列。
#
#  Related Topics 数组 哈希表 二分查找 计数 矩阵 👍 23 👎 0


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        mat.sort()
        R, C = len(mat), len(mat[0])
        for c in range(C):
            num = mat[-1][c]
            for r in range(R - 2, -1, -1):
                if num not in mat[r]:
                    break
                elif r==0:
                    return num
                else:
                    continue
        return -1


Solution().smallestCommonElement([[1195, 2657, 3608, 4285, 5154, 5299, 5497, 6960, 8125, 8294],
                                  [511, 934, 3065, 3227, 3290, 3988, 4969, 7846, 8294, 9228],
                                  [641, 1489, 2888, 3727, 4453, 5527, 6146, 6459, 8294, 9567]])
