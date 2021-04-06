'''
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import Counter
from collections import defaultdict


# 数学 二维列表 平面几何
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points = [tuple(i) for i in points]
        points_dict = Counter(points)

        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        points = list(points_dict.keys())
        lenth = len(points)
        res = 0
        if lenth == 1:
            return list(points_dict.values())[0]
        for point1_lo in range(lenth - 1):
            m = defaultdict(int)
            for point2_lo in range(point1_lo + 1, lenth):
                x1, y1 = points[point1_lo][0], points[point1_lo][1]
                x2, y2 = points[point2_lo][0], points[point2_lo][1]
                if y2 - y1 == 0:
                    slope = '0'
                elif x2 - x1 == 0:
                    slope = '00'
                else:
                    g = gcd(y2 - y1, x2 - x1)
                    slope = str(int((y2 - y1) / g)) + '/' + str(int((x2 - x1) / g))
                m[slope] = m[slope] + points_dict[points[point2_lo]]
            res = max(res, max(m.values()) + points_dict[points[point1_lo]])
        return res


a = [[1, 1], [1, 1]]
Solution().maxPoints(a)
