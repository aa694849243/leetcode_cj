'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 暴力法 caojie 5%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxacc = 0
        ans = max(prices) - prices[0]
        minprice = prices[0]
        for i in range(1, len(prices) - 1):
            if prices[i] < prices[i - 1]:  # 当出现逆序时，以该处值为第二次买入时，算其得到的最大利润
                maxacc = max(prices[i - 1] - minprice, maxacc)  # maxacc为在i处之前第一次买入卖出的最大利润
                ans = max(maxacc + max(prices[i:]) - prices[i],
                          ans)  # 两次利润的总和等于maxacc（第一次利润）+ (max(prices[i:])-prices[i])(第二次利润)
                minprice = min(minprice, prices[i])  # 更新最低点
        return ans


# 动态规划 三维动态规划
class Solution:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        length = len(prices)
        # 结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp = [[[0, 0, 0], [0, 0, 0]] for i in range(0, length)]
        # 第一天休息
        dp[0][0][0] = 0
        # 第一天买入
        dp[0][1][0] = -prices[0]
        # 第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        # 第一天不可能已经卖出
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')
        for i in range(1, length):
            # 未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0] = 0
            # 未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1] = max(dp[i - 1][1][0] + prices[i], dp[i - 1][0][1])
            # 未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2] = max(dp[i - 1][1][1] + prices[i], dp[i - 1][0][2])
            # 持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])
            # 持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][1][1])
            # 持股，卖出过2次，不可能

            dp[i][1][2] = float('-inf')
        return max(dp[length - 1][0][1], dp[length - 1][0][2], 0)

# 作者：marcusxu
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 简化版 一维动态规划
def maxProfit(self, prices: List[int]) -> int:
    one_buy = two_buy = float('inf')
    one_profit = two_profit = 0
    for p in prices:
        one_buy = min(one_buy, p)
        one_profit = max(one_profit, p - one_buy)
        two_buy = min(two_buy, p - one_profit)
        two_profit = max(two_profit, p - two_buy)
    return two_profit


Solution().maxProfit([1, 4, 1, 4, 3, 1])
