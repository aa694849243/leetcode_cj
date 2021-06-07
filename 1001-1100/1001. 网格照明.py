# -*- coding: utf-8 -*-
import collections
from typing import List


# 在 N x N 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。
#
#  数组 lamps 表示打开的灯的位置。lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的第 i 盏灯
# 。每盏灯都照亮自身单元格以及同一行、同一列和两条对角线上的所有其他单元格。
#
#  查询数组 queries 中，第 i 次查询 queries[i] = [rowi, coli]，如果单元格 [rowi, coli] 是被照亮的，则查询
# 结果为 1 ，否则为 0 。在第 i 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowi][coli] 上或其相邻 8 个方向上（与单元格
# grid[rowi][coli] 共享角或边）的任何灯。
#
#  返回答案数组 ans ， answer[i] 应等于第 i 次查询 queries[i] 的结果，1 表示照亮，0 表示未照亮。
#
#
#
#  示例 1：
#
#
# 输入：N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
# 输出：[1,0]
# 解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方框）
# 。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。
#
# 第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。
#
#
#
#  示例 2：
#
#
# 输入：N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
# 输出：[1,1]
#
#
#  示例 3：
#
#
# 输入：N = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
# 输出：[1,1,0]
#
#
#
#
#  提示：
#
#
#  1 <= N <= 109
#  0 <= lamps.length <= 20000
#  lamps[i].length == 2
#  0 <= lamps[i][j] < N
#  0 <= queries.length <= 20000
#  queries[i].length == 2
#  0 <= queries[i][j] < N
#
#  Related Topics 哈希表
#  👍 33 👎 0


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        m = collections.defaultdict(lambda: collections.Counter())
        lamps = [tuple(row) for row in lamps]
        memo = set(lamps)

        for r, c in memo:
            m['r'][r] += 1
            m['c'][c] += 1
            m['ld'][r + c] += 1
            m['rd'][c - r] += 1
        ans = []
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]

        def nei(r, c):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc

        for r, c in queries:
            if m['r'][r] > 0 or m['c'][c] > 0 or m['ld'][r + c] > 0 or m['rd'][c - r] > 0:
                ans.append(1)
            else:
                ans.append(0)
            for nr, nc in nei(r, c):
                if (nr, nc) in memo:
                    m['r'][nr] -= 1
                    m['c'][nc] -= 1
                    m['ld'][nr + nc] -= 1
                    m['rd'][nc - nr] -= 1
                memo.discard((nr, nc))
        return ans
