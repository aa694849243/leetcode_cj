'''给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

 

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

 

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1深度优先搜索dfs+置0
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or grid[0] == 0:
            return 0
        m_area = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        R = len(grid)
        C = len(grid[0])

        def dfs(i, j):
            area = 1
            grid[i][j] = 0
            for k, l in dir:
                if 0 <= i + k < R and 0 <= j + l < C and grid[i + k][j + l] == 1:
                    area += dfs(i + k, j + l)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    m_area = max(dfs(i, j), m_area)
        return m_area


# 2宽度优先遍历 广度优先遍历+队列
import collections


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or grid[0] == 0:
            return 0
        t = collections.deque()
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    t.append((i, j))
                    area = 0
                    grid[i][j] = 0
                    while t:
                        r, c = t.popleft()
                        area += 1
                        for k, l in dir:
                            if 0 <= r + k < len(grid) and 0 <= c + l < len(grid[0]) and grid[r + k][c + l] == 1:
                                t.append((r + k, c + l))
                                grid[r+k][c+l]=0
                    m_area=max(m_area,area)
        return m_area


Solution().maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])
