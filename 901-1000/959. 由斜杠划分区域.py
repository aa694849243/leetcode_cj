import collections, heapq, itertools
from typing import List


# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
#
#  （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
#
#  返回区域的数目。
#
#
#
#
#
#
#  示例 1：
#
#  输入：
# [
#   " /",
#   "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
#
#
#  示例 2：
#
#  输入：
# [
#   " /",
#   "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
#
#
#  示例 3：
#
#  输入：
# [
#   "\\/",
#   "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
#
#
#  示例 4：
#
#  输入：
# [
#   "/\\",
#   "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
#
#
#  示例 5：
#
#  输入：
# [
#   "//",
#   "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
#
#
#
#
#
#  提示：
#
#
#  1 <= grid.length == grid[0].length <= 30
#  grid[i][j] 是 '/'、'\'、或 ' '。
#
#  Related Topics 深度优先搜索 并查集 图
#  👍 259 👎 0


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        f = {}

        def find(x, y):
            f.setdefault((x, y), (x, y))
            if f[x, y] != (x, y):
                f[x, y] = find(*f[x, y])
            return f[x, y]

        def union(node1, node2):
            a = find(*node1)
            b = find(*node2)
            if a != b:
                f[b] = a

        for r in range(R := len(grid)):
            for c in range(C := len(grid[0])):
                x = r * C + c
                if grid[r][c] == ' ':
                    for _ in range(1, 4):
                        union((x, 0), (x, _))
                elif grid[r][c] == '/':
                    union((x, 0), (x, 1))
                    union((x, 2), (x, 3))
                else:
                    union((x, 0), (x, 3))
                    union((x, 1), (x, 2))
                pre1r, pre1c = r - 1, c
                pre2r, pre2c = r, c - 1
                if 0 <= pre1r < R and 0 <= pre1c < C:
                    pre1x = pre1r * C + pre1c
                    union((pre1x, 2), (x, 0))
                if 0 <= pre2r < R and 0 <= pre2c < C:
                    pre2x = pre2r * C + pre2c
                    union((pre2x, 3), (x, 1))
                for _ in range(4):
                    find(x,_)
        ans = 0
        for node, val in f.items():
            if node == val:
                ans += 1
        return ans
Solution().regionsBySlashes([" /","/ "])