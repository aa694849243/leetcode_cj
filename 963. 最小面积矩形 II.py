import collections, heapq, itertools
from typing import List


# 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。
#
#  如果没有任何矩形，就返回 0。
#
#
#
#  示例 1：
#
#
#
#  输入：[[1,2],[2,1],[1,0],[0,1]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。
#
#  示例 2：
#
#
#
#  输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
# 输出：1.00000
# 解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
#
#
#  示例 3：
#
#
#
#  输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
# 输出：0
# 解释：没法从这些点中组成任何矩形。
#
#
#  示例 4：
#
#
#
#  输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
#
#
#
#
#  提示：
#
#
#  1 <= points.length <= 50
#  0 <= points[i][0] <= 40000
#  0 <= points[i][1] <= 40000
#  所有的点都是不同的。
#  与真实值误差不超过 10^-5 的答案将视为正确结果。
#
#  Related Topics 几何 数学
#  👍 39 👎 0


# 红笔记
# 虚数的应用
# 枚举三角形
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = set(map(tuple, points))
        EPS = 1e-7
        ans = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = complex(*p3) - complex(*p1) + complex(*p2)
            if (p4.real, p4.imag) in points - {p1, p2, p3}:
                p1p2 = complex(*p2) - complex(*p1)
                p1p3 = complex(*p3) - complex(*p1)
                if abs(p1p2.real * p1p3.real + p1p2.imag * p1p3.imag) < EPS:
                    ans = min(abs(p1p2) * abs(p1p3), ans)
        return ans if ans != float('inf') else 0


# 枚举中心
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = set(map(tuple, points))
        m = collections.defaultdict(list)
        for a, b in itertools.combinations(points, 2):
            c = (complex(*a) + complex(*b)) / 2
            dis = abs(c - complex(*a))
            m[c, dis].append(a)
        ans = float('inf')
        for (c, dis), li in m.items():
            for p1, p2 in itertools.combinations(li,2):
                area = abs(complex(*p2) - complex(*p1)) * abs(complex(*p2) - (2 * c - complex(*p1)))
                ans = min(area, ans)
        return ans if ans < float('Inf') else 0

# class Solution(object):
#     def minAreaFreeRect(self, points):
#         points = [complex(*z) for z in points]
#         seen = collections.defaultdict(list)
#         for P, Q in itertools.combinations(points, 2):
#             center = (P + Q) / 2
#             radius = abs(center - P)
#             seen[center, radius].append(P)
#
#         ans = float("inf")
#         for (center, radius), candidates in seen.iteritems():
#             for P, Q in itertools.combinations(candidates, 2):
#                 ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))
#
#         return ans if ans < float("inf") else 0

Solution().minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]])
