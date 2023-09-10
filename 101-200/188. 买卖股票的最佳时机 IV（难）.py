# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
#
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
#
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
#  示例 1：
#
#
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#
#  示例 2：
#
#
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
#
#
#
#  提示：
#
#
#  1 <= k <= 100
#  1 <= prices.length <= 1000
#  0 <= prices[i] <= 1000
#
#
#  Related Topics 数组 动态规划
#  👍 989 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k <= n // 2:
            dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]
            for i in range(k):
                dp[0][i][1] = float('-inf')
            dp[0][0][1] = -prices[0]  # 2号位为卖出次数，3号位为是否持有股票
            for i in range(1, n):
                for j in range(k+1):
                    if j > 0:
                        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
            return max([dp[n - 1][i][0] for i in range(k+1)])
        else:
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            return dp[n - 1][0]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxProfit(2, [3,2,6,5,0,3]))
