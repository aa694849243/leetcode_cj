#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
#
#  要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。
#
#
#
#  示例 1：
#
#  输入：
# line1 = {0, 0}, {1, 0}
# line2 = {1, 1}, {0, -1}
# 输出： {0.5, 0}
#
#
#  示例 2：
#
#  输入：
# line1 = {0, 0}, {3, 3}
# line2 = {1, 1}, {2, 2}
# 输出： {1, 1}
#
#
#  示例 3：
#
#  输入：
# line1 = {0, 0}, {1, 1}
# line2 = {1, 0}, {2, 1}
# 输出： {}，两条线段没有交点
#
#
#
#
#  提示：
#
#
#  坐标绝对值不会超过 2^7
#  输入的坐标均是有效的二维坐标
#
#  Related Topics 几何 数学
#  👍 65 👎 0

# 1 直线参数方程
class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        def inside(x1, x2, y1, y2, xk, yk):
            return (x1 == x2 or min(x1, x2) <= xk <= max(x1, x2)) and (y1 == y2 or min(y1, y2) <= yk <= max(y1, y2))

        def update(ans, xk, yk):
            return [xk, yk] if not ans or [xk, yk] < ans else ans

        ans = []
        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2
        if (x1 - x2) * (y3 - y4) == (x3 - x4) * (y1 - y2):  # 平行的情况
            if (x3 - x1) * (y2 - y1) == (y3 - y1) * (x2 - x1):  # x3在直线x1-x2上
                if inside(x1, x2, y1, y2, x3, y3):  # 判断x3是否真的在线段x1-x2上
                    ans = update(ans, x3, y3)
                if inside(x1, x2, y1, y2, x4, y4):  # 判断x4是否在线段x1-x2上
                    ans = update(ans, x4, y4)
                if inside(x3, x4, y3, y4, x1, y1):  # 判断x1是否在线段x3-x4上
                    ans = update(ans, x1, y1)
                if inside(x3, x4, y3, y4, x2, y2):  # 判断x2是否在线段x3-x4上
                    ans = update(ans, x4, y4)
        else:
            t1 = (x3 * (y4 - y3) + y1 * (x4 - x3) - y3 * (x4 - x3) - x1 * (y4 - y3)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = (x1 * (y2 - y1) + y3 * (x2 - x1) - y1 * (x2 - x1) - x3 * (y2 - y1)) / ((x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3))
            if 0 <= t1 <= 1 and 0 <= t2 <= 1:
                ans = [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]
        return ans


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        def inside(x1, x2, y1, y2, xk, yk):
            return (x1 == x2 or min(x1, x2) <= xk <= max(x1, x2)) and (y1 == y2 or min(y1, y2) <= yk <= max(y1, y2))

        def update(ans, xk, yk):
            return [xk, yk] if not ans or [xk, yk] < ans else ans

        A, B, C, D = complex(*start1), complex(*end1), complex(*start2), complex(*end2)
        AB = B - A
        AC = C - A
        AD = D - A
        BC = C - B
        BD = D - B
        CB = B - C
        CA = A - C
        CD = D - C
        l = (AB.real * AC.imag - AB.imag * AC.real)
        r = (AB.real * AD.imag - AB.imag * AD.real)
        l_ = (CD.real * CB.imag - CD.imag * CB.real)
        r_ = (CD.real * CA.imag - CD.imag * CA.real)
        ans = []
        x1, y1 = A.real, A.imag
        x2, y2 = B.real, B.imag
        x3, y3 = C.real, C.imag
        x4, y4 = D.real, D.imag
        if l * r < 0 and l_ * r_ < 0:
            Sacd = abs(0.5 * (AC.real * AD.imag - AC.imag * AD.real))
            Sbcd = abs(0.5 * (BC.real * BD.imag - BC.imag * BD.real))
            lam = Sacd / Sbcd
            x = (x1 + lam * x2) / (1 + lam)
            y = (y1 + lam * y2) / (1 + lam)
            ans = [x, y]
        elif l * r == 0 or l_ * r_ == 0:
            if (x3 - x1) * (y2 - y1) == (y3 - y1) * (x2 - x1) and inside(x1, x2, y1, y2, x3, y3):
                ans = update(ans, x3, y3)
            if (x4 - x1) * (y2 - y1) == (y4 - y1) * (x2 - x1) and inside(x1, x2, y1, y2, x4, y4):
                ans = update(ans, x4, y4)
            if (x1 - x3) * (y4 - y3) == (y1 - y3) * (x4 - x3) and inside(x3, x4, y3, y4, x1, y1):
                ans = update(ans, x1, y1)
            if (x2 - x3) * (y4 - y3) == (y2 - y3) * (x4 - x3) and inside(x3, x4, y3, y4, x2, y2):
                ans = update(ans, x2, y2)
        return ans


Solution().intersection([0, 0], [1, 0], [1, 1], [0, -1])
