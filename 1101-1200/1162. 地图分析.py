# -*- coding: utf-8 -*-
from typing import List


# 你现在手里有一份大小为 N x N 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的。
#
# 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。
#
# 如果网格上只有陆地或者海洋，请返回 -1。
#
#  
#
# 示例 1：
#
#
#
# 输入：[[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释：
# 海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。
# 示例 2：
#
#
#
# 输入：[[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释：
# 海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。
#  
#
# 提示：
#
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] 不是 0 就是 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0]),
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        t = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    t.append((i, j))
        if len(t) == 0 or len(t) == R * C:
            return -1
        step = 0
        while True:
            tree = []
            for r, c in t:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                        tree.append((nr, nc))
                        grid[nr][nc] = 2
            if not tree:
                break
            step += 1
            t = tree
        return step
Solution().maxDistance([[1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0],[1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1],[0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0],[0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1],[1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0],[0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0],[1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1],[0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],[0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0],[0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0],[0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1],[1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1],[1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0],[1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1],[0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0]])