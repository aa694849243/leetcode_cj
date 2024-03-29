# -*- coding: utf-8 -*-
import fractions
from typing import List


# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为
#  x、纵坐标为 y 的点。
#
#  请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
#
#
#
#  示例 1：
#
#
#
#  输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
#
#
#  示例 2：
#
#
#
#  输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
#
#
#
#
#  提示：
#
#
#  2 <= coordinates.length <= 1000
#  coordinates[i].length == 2
#  -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#  coordinates 中不含重复的点
#
#  Related Topics 几何 数组 数学
#  👍 87 👎 0
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x2 - x1 != 0:
            k = fractions.Fraction(y2 - y1, x2 - x1)
            for x, y in coordinates[2:]:
                if x==x1:
                    return False
                a = fractions.Fraction(y - y1, x - x1)
                if k != a:
                    return False
            return True
        else:
            for x, y in coordinates[2:]:
                if x!=x1:
                    return False
            return True
