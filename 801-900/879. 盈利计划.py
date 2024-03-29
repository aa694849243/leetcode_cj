# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
#
#  第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
#
#  工作的任何至少产生 minProfit 利润的子集称为盈利计划。并且工作的成员总数最多为 n 。
#
#  有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
#
#
#
#
#
#  示例 1：
#
#
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
#
#  示例 2：
#
#
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
#
#
#
#
#
#  提示：
#
#
#  1 <= n <= 100
#  0 <= minProfit <= 100
#  1 <= group.length <= 100
#  1 <= group[i] <= 100
#  profit.length == group.length
#  0 <= profit[i] <= 100
#
#  Related Topics 动态规划
#  👍 68 👎 0

from typing import List


# 用模板做 答案正确，但超时了
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        a = sum(profit)
        dp = [[0] * (a + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i, num in enumerate(group):
            for j in range(n, num - 1, -1):
                for k in range(a, profit[i] - 1, -1):
                    dp[j][k] += dp[j - num][k - profit[i]]
                    dp[j][k] %= mod
        return sum(dp[i][j] for i in range(n + 1) for j in range(minProfit, a + 1)) % mod


# 顺着做，需要做两个dp，因为是0-1背包，防止覆盖 多限制条件动态规划
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i, num in enumerate(group):
            dp2 = [row[:] for row in dp] #每一轮加入一个group更新dp
            for j in range(n, num - 1, -1):
                for k in range(minProfit + 1):
                    p = min(minProfit, k + profit[i])
                    dp2[j][p] += dp2[j - num][k]
            dp=dp2
        return sum(dp[i][-1] for i in range(n+1)) % mod


Solution().profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8])
