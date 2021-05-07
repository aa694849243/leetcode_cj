# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
#
#
#
#  注意:
#
#
#  3 <= points.length <= 50.
#  不存在重复的点。
#  -50 <= points[i][j] <= 50.
#  结果误差值在 10^-6 以内都认为是正确答案。
#
#  Related Topics 数学
#  👍 73 👎 0


from typing import List

import itertools


# 1sin公式
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def sin(a, b, c):  # sinb的值
            return (a[0] - b[0]) * (c[1] - b[1]) - (c[0] - b[0]) * (a[1] - b[1])

        def area(a, b, c):
            return .5 * abs(sin(a, b, c))

        # ca,cb,sin
        # li=[]
        # for trangle in itertools.combinations(points,3):
        #     li.append(area(*trangle))
        return max(area(*trangle) for trangle in itertools.combinations(points, 3))


# 海伦公式
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def length(a,b):
            return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
        def area(a,b,c):
            x=length(a,b)
            y=length(b,c)
            z=length(a,c)
            p=.5*(x+y+z)
            ans=(p*(p-x)*(p-y)*(p-z))
            return ans**.5 if ans>0 else 0
        li=[]
        for trangle in itertools.combinations(points,3):
            li.append(area(*trangle))
        return max(area(*trangle) for trangle in itertools.combinations(points, 3))
#3鞋带公式
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a, b, c):
            return .5*abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-a[1]*b[0]-b[1]*c[0]-c[1]*a[0])

        # ca,cb,sin
        # li=[]
        # for trangle in itertools.combinations(points,3):
        #     li.append(area(*trangle))
        return max(area(*trangle) for trangle in itertools.combinations(points, 3))

Solution().largestTriangleArea([[35,33],[-19,42],[11,47],[11,37]] )
