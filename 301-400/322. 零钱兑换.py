'''给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

 

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
 

说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        if not coins or min(coins)>amount:
            return -1
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if j > i:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1] if dp[-1]!=float('inf') else -1

##动态规划 背包问题 完全背包 可重复数组
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1


coins=[1,2,3]
n=4
Solution().coinChange(coins,n)