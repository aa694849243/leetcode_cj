import collections, heapq, itertools
from typing import List


# 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。
#
#  如果没有任何矩形，就返回 0。
#
#
#
#  示例 1：
#
#  输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
# 输出：4
#
#
#  示例 2：
#
#  输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= points.length <= 500
#  0 <= points[i][0] <= 40000
#  0 <= points[i][1] <= 40000
#  所有的点都是不同的。
#
#  Related Topics 哈希表
#  👍 79 👎 0


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        m = collections.defaultdict(set)
        for i, j in points:
            m[i].add(j)
        ans = float('inf')
        X = sorted(m.keys())
        for l in range(len(X) - 1):
            for r in range(l + 1, len(X)):
                li = sorted(list(m[X[l]] & m[X[r]]))
                if len(li) <= 1:
                    continue
                widths = [li[i] - li[i - 1] for i in range(1, len(li))]
                ans = min([ans] + [width * (X[r] - X[l]) for width in widths])
        return ans if ans != float('inf') else 0
