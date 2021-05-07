# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 国际象棋中的骑士可以按下图所示进行移动：
#
#  .
#
#
# 这一次，我们将 “骑士” 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳 N-1 步。每一步必须是从一个数字键跳到另一个数字键。
#
#  每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下 N 位数字。
#
#  你能用这种方式拨出多少个不同的号码？
#
#  因为答案可能很大，所以输出答案模 10^9 + 7。
#
#
#
#
#
#
#  示例 1：
#
#  输入：1
# 输出：10
#
#
#  示例 2：
#
#  输入：2
# 输出：20
#
#
#  示例 3：
#
#  输入：3
# 输出：46
#
#
#
#
#  提示：
#
#
#  1 <= N <= 5000
#
#  Related Topics 动态规划
#  👍 77 👎 0


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        dp = [1] * 10
        dp[5] = 0
        mod = 10 ** 9 + 7
        for _ in range(n - 1):
            dp2 = [1] * 10
            dp2[0] = dp[4] + dp[6]
            dp2[1] = dp[8] + dp[6]
            dp2[2] = dp[7] + dp[9]
            dp2[3] = dp[8] + dp[4]
            dp2[4] = dp[3] + dp[0] + dp[9]
            dp2[6] = dp[7] + dp[1] + dp[0]
            dp2[7] = dp[2] + dp[6]
            dp2[8] = dp[1] + dp[3]
            dp2[9] = dp[4] + dp[2]
            dp = dp2
        return (sum(dp)-1) % mod


Solution().knightDialer(3)
