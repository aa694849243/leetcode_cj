#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你两个 稀疏矩阵 A 和 B，请你返回 AB 的结果。你可以默认 A 的列数等于 B 的行数。
#
#  请仔细阅读下面的示例。
#
#
#
#  示例：
#
#  输入：
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
# 输出：
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
#
#  Related Topics 数组 哈希表 矩阵
#  👍 60 👎 0

# https://leetcode-cn.com/problems/sparse-matrix-multiplication/solution/python-100shi-jian-by-austinzy-q7z4/
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        R1, C1 = len(mat1), len(mat1[0])
        R2, C2 = len(mat2), len(mat2[0])
        res = [[0] * C2 for _ in range(R1)]
        mat1_ = collections.defaultdict(dict)
        mat2_ = collections.defaultdict(dict)
        for r in range(R1):
            for c in range(C1):
                if mat1[r][c]:
                    mat1_[r][c] = mat1[r][c]
        for r in range(R2):
            for c in range(C2):
                if mat2[r][c]:
                    mat2_[c][r] = mat2[r][c]
        for k1, v1 in mat1_.items():
            for k2, v2 in mat2_.items():
                res[k1][k2] = sum(v * v2.get(k, 0) for k, v in v1.items())
        return res
