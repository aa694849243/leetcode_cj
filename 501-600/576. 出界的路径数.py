'''给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

 

示例 1：

输入: m = 2, n = 2, N = 2, i = 0, j = 0
输出: 6
解释:

示例 2：

输入: m = 1, n = 3, N = 3, i = 0, j = 1
输出: 12
解释:

 

说明:

球一旦出界，就不能再被移动回网格内。
网格的长度和高度在 [1,50] 的范围内。
N 在 [0,50] 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/out-of-boundary-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1动态规划
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(N + 1)]
        for k in range(n + 1):  # 因为只能上下左右四个方向移动，四个角的值无法传递到矩阵中,不必特地排除四个角
            dp[0][0][k] = 1
            dp[0][m + 1][k] = 1
        for k in range(m + 1):
            dp[0][k][0] = 1
            dp[0][k][n + 1] = 1
        for k in range(1, N + 1):
            for r in range(1, m + 1):
                for c in range(1, n + 1):
                    dp[k][r][c] = dp[k - 1][r - 1][c] + dp[k - 1][r + 1][c] + dp[k - 1][r][c - 1] + dp[k - 1][r][c + 1]
        ans = 0
        for k in range(1, N + 1):
            ans += dp[k][i + 1][j + 1]
        return ans % (10 ** 9 + 7)


# 2递归
import functools


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @functools.lru_cache(None)
        def rec(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if k == 0:
                return 0
            return rec(i-1,j,k-1)+rec(i+1,j,k-1)+rec(i,j-1,k-1)+rec(i,j+1,k-1)
        return rec(i,j,N)%(10**9+7)


Solution().findPaths(2, 2, 1, 0, 0)
