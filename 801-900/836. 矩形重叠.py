# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于 x
# 轴，左右边平行于 y 轴。
#
#  如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
#
#  给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。
#
#
#
#  示例 1：
#
#
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
#
#
#  示例 3：
#
#
# 输入：rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# 输出：false
#
#
#
#
#  提示：
#
#
#  rect1.length == 4
#  rect2.length == 4
#  -109 <= rec1[i], rec2[i] <= 109
#  rec1[0] <= rec1[2] 且 rec1[1] <= rec1[3]
#  rec2[0] <= rec2[2] 且 rec2[1] <= rec2[3]
#
#  Related Topics 数学
#  👍 201 👎 0

from typing import List


# 1普通方法
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if x3 <= x1 and x4 <= x1:
            return False
        if x3 >= x2 and x4 >= x2:
            return False
        if y3 <= y1 and y4 <= y1:
            return False
        if y3 >= y2 and y4 >= y2:
            return False
        return True


# 2逆向思维
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if x1 == x2 or y1 == y2 or x3 == x4 or y3 == y4:
            return False
        return not (x3 >= x2 or x1 >= x4 or y1 >= y4 or y2 <= y3)


# 3线段投影
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersect(l1, r1, l2, r2):
            return min(r1, r2) > max(l1, l2)

        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return intersect(x1, x2, x3, x4) and intersect(y1, y2, y3, y4)
