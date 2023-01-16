# -*- coding: utf-8 -*-
# 一张桌子上总共有 n 个硬币 栈 。每个栈有 正整数 个带面值的硬币。
#
#  每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里。
#
#  给你一个列表 piles ，其中 piles[i] 是一个整数数组，分别表示第 i 个栈里 从顶到底 的硬币面值。同时给你一个正整数 k ，请你返回在 恰
# 好 进行 k 次操作的前提下，你钱包里硬币面值之和 最大为多少 。
#
#
#
#  示例 1：
#
#
#
#
# 输入：piles = [[1,100,3],[7,8,9]], k = 2
# 输出：101
# 解释：
# 上图展示了几种选择 k 个硬币的不同方法。
# 我们可以得到的最大面值为 101 。
#
#
#  示例 2：
#
#
# 输入：piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
# 输出：706
# 解释：
# 如果我们所有硬币都从最后一个栈中取，可以得到最大面值和。
#
#
#
#
#  提示：
#
#
#  n == piles.length
#  1 <= n <= 1000
#  1 <= piles[i][j] <= 10⁵
#  1 <= k <= sum(piles[i].length) <= 2000
#
#
#  Related Topics 数组 动态规划 前缀和
#  👍 47 👎 0

from typing import List
import functools


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        precums = []
        for i in range(len(piles)):
            precums.append([piles[i][0]])
            for j in range(1, len(piles[i])):
                precums[i].append(precums[i][-1] + piles[i][j])
        @functools.lru_cache(None)
        def dp(cur_i, sum_k):
            if sum_k == 0:
                return 0
            if cur_i == 0:
                if sum_k <= len(precums[cur_i]):
                    return precums[cur_i][sum_k - 1]
                else:
                    return float('-inf')
            res = 0
            for cur_k in range(min(sum_k, len(precums[cur_i])) + 1):
                if cur_k == 0:
                    res = max(res, dp(cur_i - 1, sum_k))
                else:
                    res = max(res, dp(cur_i - 1, sum_k - cur_k) + precums[cur_i][cur_k - 1])
            return res

        return dp(n - 1, k)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2))
