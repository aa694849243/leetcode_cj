'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 官方解答 6大类型 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-w-5/
# 解答参考 123题
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k <= n // 2:
            dp = [[[float('-inf')] * (k+1), [float('-inf')] * (k+1)] for _ in range(n)]
            dp[0][0][0]=0
            dp[0][1][0] = -prices[0]
            for i in range(1,n):
                for m in range(k+1):
                    dp[i][1][m] = max(dp[i - 1][1][m], dp[i - 1][0][m] - prices[i])  # m为卖出次数
                    dp[i][0][m] = max(dp[i - 1][0][m], dp[i - 1][1][m - 1] + prices[i])
                    dp[i][0][0]=0
            return max(max(dp[-1][0][m] for m in range(k+1)), 0)
        else:
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            return max(dp[-1][0], 0)


k = 4
prices = [1,2,4,2,5,7,2,4,9,0]
Solution().maxProfit(k, prices)
