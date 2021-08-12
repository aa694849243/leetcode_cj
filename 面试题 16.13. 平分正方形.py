#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。
#
#  每个正方形的数据square包含3个数值，正方形的左下顶点坐标[X,Y] = [square[0],square[1]]，以及正方形的边长square[2
# ]。所求直线穿过两个正方形会形成4个交点，请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点
# ）。2个端点坐标[X1,Y1]和[X2,Y2]的返回格式为{X1,Y1,X2,Y2}，要求若X1 != X2，需保证X1 < X2，否则需保证Y1 <= Y2。
#
#
#  若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。
#
#  示例：
#
#  输入：
# square1 = {-1, -1, 2}
# square2 = {0, -1, 2}
# 输出： {-1,0,2,0}
# 解释： 直线 y = 0 能将两个正方形同时分为等面积的两部分，返回的两线段端点为[-1,0]和[2,0]
#
#
#  提示：
#
#
#  square.length == 3
#  square[2] > 0
#
#  Related Topics 几何 数学
#  👍 9 👎 0

# 正方形中点，上下交左右交
class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        s1x, s1y = square1[0] + square1[2] / 2, square1[1] + square1[2] / 2
        s2x, s2y = square2[0] + square2[2] / 2, square2[1] + square2[2] / 2
        x1l, y1l = square1[:2]
        x1r, y1r = square1[0] + square1[2], square1[1] + square1[2]
        x2l, y2l = square2[:2]
        x2r, y2r = square2[0] + square2[2], square2[1] + square2[2]
        x_, y_ = s2x - s1x, s2y - s1y
        lx = sorted([x1l, x1r, x2l, x2r])
        ly = sorted([y1l, y1r, y2l, y2r])
        if x_ != 0:
            k = y_ / x_
            b = s1y - s1x * k
            if abs(k) <= 1:
                x1, x2 = lx[0], lx[-1]
                y1, y2 = x1 * k + b, x2 * k + b
            else:
                y1, y2 = ly[0], ly[-1]
                x1, x2 = (y1 - b) / k, (y2 - b) / k
                if x1 > x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
        else:
            x = s1x
            x1, x2 = x, x
            y1, y2 = ly[0], ly[-1]
        return [x1, y1, x2, y2]


Solution().cutSquares([249, -199, 5], [-1, 136, 76])
