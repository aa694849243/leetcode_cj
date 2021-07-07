# -*- coding: utf-8 -*-
from typing import List


# 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：
#
#
#  1 表示连接左单元格和右单元格的街道。
#  2 表示连接上单元格和下单元格的街道。
#  3 表示连接左单元格和下单元格的街道。
#  4 表示连接右单元格和下单元格的街道。
#  5 表示连接左单元格和上单元格的街道。
#  6 表示连接右单元格和上单元格的街道。
#
#
#
#
#  你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径
# 。该路径必须只沿着街道走。
#
#  注意：你 不能 变更街道。
#
#  如果网格中存在有效的路径，则返回 true，否则返回 false 。
#
#
#
#  示例 1：
#
#
#
#  输入：grid = [[2,4,3],[6,5,2]]
# 输出：true
# 解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
#
#
#  示例 2：
#
#
#
#  输入：grid = [[1,2,1],[1,2,1]]
# 输出：false
# 解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
#
#
#  示例 3：
#
#  输入：grid = [[1,1,2]]
# 输出：false
# 解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
#
#
#  示例 4：
#
#  输入：grid = [[1,1,1,1,1,1,3]]
# 输出：true
#
#
#  示例 5：
#
#  输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
# 输出：true
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 300
#  1 <= grid[i][j] <= 6
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 44 👎 0


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                f[b] = a

        def cal(r, c):
            return r * C + c

        def judge(a, b, dir):
            if dir == 0:  # 左右
                if b in (1, 3, 5):
                    return a in (1, 4, 6)
            elif dir == 1:  # 上下
                if b in (2, 5, 6):
                    return a in (2, 3, 4)

        for r in range(R):
            for c in range(C):
                node = cal(r, c)
                for i, (pr, pc) in enumerate([(r, c - 1), (r - 1, c)]):
                    if 0 <= pr < R and 0 <= pc < C:
                        a = grid[pr][pc]
                        b = grid[r][c]
                        if judge(a, b, i):
                            p = cal(pr, pc)
                            union(p, node)
        s=0
        e=R*C-1
        return find(s)==find(e)
Solution().hasValidPath([[2],[2],[2],[2],[2],[2],[6]])