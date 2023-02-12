# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 19:46 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != inf else -1
# leetcode submit region end(Prohibit modification and deletion)

