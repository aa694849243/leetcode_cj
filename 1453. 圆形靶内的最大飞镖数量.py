#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Tuple

# 墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。
#
#  投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。
#
#  请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。
#
#
#
#  示例 1：
#
#
#
#  输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
# 输出：4
# 解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
#
#
#  示例 2：
#
#
#
#  输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
# 输出：5
# 解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
#
#  示例 3：
#
#  输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
# 输出：1
#
#
#  示例 4：
#
#  输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= points.length <= 100
#  points[i].length == 2
#  -10^4 <= points[i][0], points[i][1] <= 10^4
#  1 <= r <= 5000
#
#  Related Topics 几何 数组 数学
#  👍 22 👎 0

import itertools
import math


# 1 穷举法
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def helper(a: complex, b: complex, r: int) -> Tuple[complex, complex]:
            ab = b - a
            mid = (a + b) / 2
            dist_c_mid = math.sqrt(r ** 2 - (abs(ab) / 2) ** 2)
            c_mid, mid_c = complex(-ab.imag, ab.real), complex(ab.imag, -ab.real)
            c_mid, mid_c = c_mid / abs(c_mid) * dist_c_mid, mid_c / abs(mid_c) * dist_c_mid
            return mid + c_mid, mid + mid_c

        points = [complex(*lst) for lst in points]
        res = 0
        eps = 1e-8
        for a, b in itertools.combinations(points, 2):
            if abs(b - a) > 2 * r:
                continue
            c1, c2 = helper(a, b, r)
            cnt_c1, cnt_c2 = 0, 0
            for point in points:
                if abs(abs(point - c1)) - r < eps:
                    cnt_c1 += 1
                if abs(abs(point - c2)) - r < eps:
                    cnt_c2 += 1
            res = max(res, cnt_c1, cnt_c2)
        return max(res, +(len(points) > 0))


# 2 angular sweep
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:

        


Solution().numPoints(points=[[-2, 0], [2, 0], [0, 2], [0, -2]], r=2)
