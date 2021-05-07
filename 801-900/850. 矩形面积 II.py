# 我们给出了一个（轴对齐的）矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2, y2]，其中（x1，y1）是矩形
#  i 左下角的坐标，（x2，y2）是该矩形右上角的坐标。
#
#  找出平面中所有矩形叠加覆盖后的总面积。 由于答案可能太大，请返回它对 10 ^ 9 + 7 取模的结果。
#
#
#
#  示例 1：
#
#  输入：[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# 输出：6
# 解释：如图所示。
#
#
#  示例 2：
#
#  输入：[[0,0,1000000000,1000000000]]
# 输出：49
# 解释：答案是 10^18 对 (10^9 + 7) 取模的结果， 即 (10^9)^2 → (-7)^2 = 49 。
#
#
#  提示：
#
#
#  1 <= rectangles.length <= 200
#  rectanges[i].length = 4
#  0 <= rectangles[i][j] <= 10^9
#  矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。
#
#  Related Topics 线段树 Line Sweep
#  👍 72 👎 0
# 线段树
from typing import List

# 1容斥原理
import functools
import collections
import itertools


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7

        def intersect(rec1, rec2):
            return max(rec1[0], rec2[0]), max(rec1[1], rec2[1]), min(rec1[2], rec2[2]), min(rec1[3], rec2[3])

        def area(x1, y1, x2, y2):
            return max(0, x2 - x1) * max(0, y2 - y1)  # 如果不相交则面积为0

        ans = 0
        for size in range(1, len(rectangles) + 1):
            for group in itertools.combinations(rectangles, size):
                ans += (-1) ** (size + 1) * area(*functools.reduce(intersect, group))
        return ans % mod


# 2坐标压缩
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        X = set()
        Y = set()
        for rect in rectangles:
            X |= {rect[0], rect[2]}
            Y |= {rect[1], rect[3]}
        X = sorted(X)
        Y = sorted(Y)
        mapx = {x: i for i, x in enumerate(X)}
        mapy = {y: i for i, y in enumerate(Y)}
        grid = [[0] * len(Y) for _ in range(len(X))]
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            for i in range(mapx[x1], mapx[x2]):
                for j in range(mapy[y1], mapy[y2]):
                    grid[i][j] = 1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans += (X[i + 1] - X[i]) * (Y[j + 1] - Y[j])
        return ans % mod


# 3扫描线
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        open, close = 0, 1
        m = set()
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            m |= {(y1, 0, x1, x2), (y2, 1, x1, x2)}
        m = sorted(m)
        active = []

        def quiry():
            length = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                length += max(0, x2 - cur)
                cur = max(cur, x2)
            return length

        cur = 0
        ans = 0
        for y, status, x1, x2 in m:
            ans += quiry() * (y - cur)
            if status == open:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))
            cur = y
        return ans % mod


# 4扫描线+线段树 插入区间
class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def update(self, i, j, val):
        if i >= j: return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total

class Solution(object):
    def rectangleArea(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        global X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X)-1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(Xi[x1], Xi[x2], typ) if x1!=x2 else cur_x_sum
            cur_y = y

        return ans % (10**9 + 7)


Solution().rectangleArea([[5,0,10,20],[5,0,5,10]])
