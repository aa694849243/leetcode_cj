'''

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
'''
from typing import List

#类似84题解法
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[] for _ in range(rows)]
        dpright = [[cols] * cols for _ in range(rows)]
        for i in range(rows):
            stack = []
            for j in range(cols):
                if i == 0:
                    matrix[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]):
                    matrix[i][j] = int(matrix[i - 1][j]) + 1
                else:
                    matrix[i][j] = 0
                if j == 0:
                    dp[i].append(-1)
                    stack.append(j)
                elif matrix[i][j] > matrix[i][j - 1]:
                    stack.append(j)
                    dp[i].append(j - 1)
                else:
                    while stack and matrix[i][stack[-1]] >= matrix[i][j]:
                        x = stack.pop()
                        dpright[i][x] = j
                    if not stack:
                        dp[i].append(-1)
                    else:
                        dp[i].append(stack[-1])
                    stack.append(j)
        maxarea = 0
        for i in range(rows):
            for j in range(cols):
                maxarea = max(maxarea, matrix[i][j] * (dpright[i][j] - dp[i][j] - 1))
        return maxarea


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
Solution().maximalRectangle(matrix)
