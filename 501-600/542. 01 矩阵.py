'''给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

 

示例 1：

输入：
[[0,0,0],
 [0,1,0],
 [0,0,0]]

输出：
[[0,0,0],
 [0,1,0],
 [0,0,0]]
示例 2：

输入：
[[0,0,0],
 [0,1,0],
 [1,1,1]]

输出：
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

提示：

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 1宽度优先搜索 广度优先搜索
import collections


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) == 0:
            return matrix
        visted = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        q = collections.deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    visted[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            step = visted[x][y] + 1
            for i, j in dirs:
                x_new = i + x
                y_new = j + y
                if 0 <= x_new < rows and 0 <= y_new < cols and visted[x_new][y_new] == -1:
                    visted[x_new][y_new] = step
                    q.append((x_new, y_new))
        return visted


# 2动态规划
# 左下，右上四个反向
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) == 0:
            return matrix
        dp = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
        for i in range(rows):  # 从左往右从上到下扫描
            for j in range(cols):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i + 1 < rows:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < cols:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp


Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
