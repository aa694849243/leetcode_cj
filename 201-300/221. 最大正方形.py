'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix[0])==0:
            return 0
        cols, rows = len(matrix[0]), len(matrix)
        dp = [[0] * cols for _ in range(rows)]
        ans=0
        for i in range(cols):
            dp[0][i] = int(matrix[0][i])
            ans=max(ans,dp[0][i])
        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
            ans=max(dp[i][0],ans)
        if cols < 2 or rows < 2:
            return ans
        for i in range(1, rows):
            for j in range(1, cols):
                if int(matrix[i][j]) == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(int(dp[i - 1][j - 1]), int(dp[i - 1][j]), int(dp[i][j - 1])) + 1
                    ans = max(ans, dp[i][j])
        return ans**2
a=[["0","1"]]
Solution().maximalSquare(a)