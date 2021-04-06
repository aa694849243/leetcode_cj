'''给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

 

提示：

输出坐标的顺序不重要
m 和 n 都小于150
 

示例：

 

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# 深度优先搜索 逆流
from typing import List


class Solution:
    def __init__(self):
        self.matrix = []
        self.visted = []
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.cols = 0
        self.rows = 0
        self.res = []

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        self.matrix = matrix
        self.cols, self.rows = len(matrix[0]), len(matrix)
        pa, at = [[False] * self.cols for _ in range(self.rows)], [[False] * self.cols for _ in range(self.rows)]

        def dfs(i, j, flag):
            if self.visted[i][j]:
                return
            if flag:  # 流向太平洋
                pa[i][j] = True
            else:  # 流向大西洋
                at[i][j] = True
            self.visted[i][j] = True
            for dir in self.dirs:
                newx, newy = i + dir[0], j + dir[1]
                if newx < 0 or newy < 0 or newx >= self.rows or newy >= self.cols:
                    continue
                if self.matrix[newx][newy] < self.matrix[i][j]:
                    continue
                dfs(newx, newy, flag)

        self.visted = [[False] * self.cols for _ in range(self.rows)]
        for i in range(self.cols):  # 逆流入上方太平洋
            dfs(0, i, flag=True)

        self.visted = [[False] * self.cols for _ in range(self.rows)]
        for i in range(self.cols):  # 逆流入下方大西洋
            dfs(self.rows - 1, i, flag=False)

        self.visted = [[False] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):  # 逆流入左边太平洋
            dfs(i, 0, flag=True)

        self.visted = [[False] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):  # 逆流入右边大西洋
            dfs(i, self.cols - 1, flag=False)

        for i in range(self.rows):
            for j in range(self.cols):
                if pa[i][j] and at[i][j]:
                    self.res.append([i, j])
        return self.res
matrix=[[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]]
Solution().pacificAtlantic(matrix)