'''有两种形状的瓷砖：一种是 2x1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。

XX  <- 多米诺

XX  <- "L" 托米诺
X
给定 N 的值，有多少种方法可以平铺 2 x N 的面板？返回值 mod 10^9 + 7。

（平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。）

示例:
输入: 3
输出: 5
解释:
下面列出了五种不同的方法，不同字母代表不同瓷砖：
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
提示：

N  的范围是 [1, 1000]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/domino-and-tromino-tiling
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1动态规划状态转移 需要注意瓷砖奇偶问题
class Solution:
    def numTilings(self, N: int) -> int:
        dp = [1, 0, 0, 0]
        mod = 10 ** 9 + 7
        ndp = [0, 0, 0, 0]
        for _ in range(N):
            ndp[0] = (dp[0] + dp[3]) % mod
            ndp[1] = (dp[0] + dp[2]) % mod
            ndp[2] = (dp[0] + dp[1]) % mod
            ndp[3] = (dp[0] + dp[1] + dp[2]) % mod
            dp = ndp.copy()
        return dp[0]




# 2矩阵求幂
class Solution:
    def numTilings(self, N: int) -> int:
        mod = 10**9 + 7
        matrix = [[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 0]]

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            m = [[sum(a * b for a, b in zip(row, col)) % mod for col in ZB] for row in A]
            return m

        def matrix_powerk(matrix, k):
            if k == 0:  # 矩阵的0次方为单位矩阵
                return [[+(i == j) for i in range(len(matrix))] for j in range(len(matrix))]
            if k == 1:
                return matrix
            elif k % 2:
                return matrix_mult(matrix_powerk(matrix, k - 1), matrix)
            b = matrix_mult(matrix, matrix)
            return matrix_powerk(b, k // 2)
        return matrix_powerk(matrix, N)[0][0]

Solution().numTilings(4)
