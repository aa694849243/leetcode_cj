#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。
#
#
#
#  示例 1：
#
#
# 输入：mat = [[1,0,1],
#             [1,1,0],
#             [1,1,0]]
# 输出：13
# 解释：
# 有 6 个 1x1 的矩形。
# 有 2 个 1x2 的矩形。
# 有 3 个 2x1 的矩形。
# 有 1 个 2x2 的矩形。
# 有 1 个 3x1 的矩形。
# 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
#
#
#  示例 2：
#
#
# 输入：mat = [[0,1,1,0],
#             [0,1,1,1],
#             [1,1,1,0]]
# 输出：24
# 解释：
# 有 8 个 1x1 的子矩形。
# 有 5 个 1x2 的子矩形。
# 有 2 个 1x3 的子矩形。
# 有 4 个 2x1 的子矩形。
# 有 2 个 2x2 的子矩形。
# 有 2 个 3x1 的子矩形。
# 有 1 个 3x2 的子矩形。
# 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
#
#
#  示例 3：
#
#
# 输入：mat = [[1,1,1,1,1,1]]
# 输出：21
#
#
#  示例 4：
#
#
# 输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= rows <= 150
#  1 <= columns <= 150
#  0 <= mat[i][j] <= 1
#
#  Related Topics 栈 数组 动态规划 矩阵 单调栈
#  👍 120 👎 0


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        for row in mat:
            for c in range(len(row)):
                if c == 0 or row[c] == 0:
                    continue
                else:
                    row[c] = row[c - 1] + 1
        res = 0
        R, C = len(mat), len(mat[0])
        for r in range(R):
            for c in range(C):
                tmp = mat[r][c]
                for p in range(r, -1, -1):
                    tmp = min(mat[p][c], tmp)
                    if tmp == 0:
                        break
                    res += tmp
        return res


Solution().numSubmat([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]])
