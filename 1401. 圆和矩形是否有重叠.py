# -*- coding: utf-8 -*-
# 给你一个以 (radius, x_center, y_center) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1, y
# 1) 是矩形左下角的坐标，(x2, y2) 是右上角的坐标。
#
#  如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。
#
#  换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。
#
#
#
#  示例 1：
#
#
#
#  输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# 输出：true
# 解释：圆和矩形有公共点 (1,0)
#
#
#  示例 2：
#
#
#
#  输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# 输出：true
#
#
#  示例 3：
#
#
#
#  输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
# 输出：true
#
#
#  示例 4：
#
#  输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= radius <= 2000
#  -10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
#  x1 < x2
#  y1 < y2
#
#  Related Topics 几何 数学
#  👍 25 👎 0

# 1九宫格模拟
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def check(x, y):
            return (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2

        l, r, u, d = x1, x2, y2, y1
        if x_center <= l:
            if y_center >= u:
                return check(l, u)  # 左上
            elif y_center <= d:
                return check(l, d)  # 左下
            else:
                return check(l, y_center)  # 左中
        if x_center >= r:
            if y_center >= u:
                return check(r, u)  # 右上
            elif y_center <= d:
                return check(r, d)  # 右下
            else:
                return check(r, y_center)  # 右中
        if y_center >= u:
            return check(x_center, u)  # 中上
        elif y_center <= d:
            return check(x_center, d)  # 中下
        else:
            return True  # 中中


# 2数学
# https://www.zhihu.com/question/24251545
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # 设矩形中心为c,右上角为r，圆心为p
        cp = complex(abs(x_center - mx), abs(y_center - my))  # 矩形中心到圆心的向量，取绝对值将四个象限的圆全都映射到第一象限
        r = complex(mx, my)
        cr = complex(x2, y2) - r  # 矩形中心到矩形右上角向量
        rp = cp - cr  # 矩形右上角到圆心的向量
        x, y = rp.real, rp.imag
        x = x if x > 0 else 0
        y = y if y > 0 else 0
        return abs(complex(x, y)) <= radius


Solution().checkOverlap(1,0, 0, 2 ,-10, 3, 10)
