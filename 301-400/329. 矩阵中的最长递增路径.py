'''给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j, l):
            l += 1
            n = 0
            for dir in dirs:
                if 0 <= i + dir[0] < row and 0 <= j + dir[1] < col and matrix[i + dir[0]][j + dir[1]] > matrix[i][
                    j] and not visted[i + dir[0]][j + dir[1]]:
                    if visted2[i + dir[0]][j + dir[1]] != -1:
                        n = max(n, visted2[i + dir[0]][j + dir[1]])
                    else:
                        visted[i + dir[0]][j + dir[1]] = 1
                        n = max(n, dfs(i + dir[0], j + dir[1], 0))
                        visted[i + dir[0]][j + dir[1]] = 0
            visted2[i][j] = l + n
            return l + n
        if not matrix or not len(matrix[0]):
            return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visted = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        visted2 = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        m = 0
        row, col = len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if visted2[i][j] == -1:
                    visted[i][j] = 1
                    m = max(m, dfs(i, j, 0))
                    visted[i][j] = 0
        return m




a = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Solution().longestIncreasingPath(a)