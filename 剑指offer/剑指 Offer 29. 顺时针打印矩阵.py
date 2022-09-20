#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#
#
#  示例 1：
#
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
#  示例 2：
#
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
#  限制：
#
#
#  0 <= matrix.length <= 100
#  0 <= matrix[i].length <= 100
#
#
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
#  Related Topics 数组 矩阵 模拟
#  👍 276 👎 0


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = [matrix[0][0]]
        R, C = len(matrix), len(matrix[0]),
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        visted = {(0, 0)}
        r, c = 0, 0
        while len(visted) < R * C:
            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc
            if nr in (R,-1) or nc in (C,-1) or (nr, nc) in visted:
                d += 1
                d %= 4
                continue
            visted.add((nr, nc))
            ans.append(matrix[nr][nc])
            r, c = nr, nc,
        return ans


Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
