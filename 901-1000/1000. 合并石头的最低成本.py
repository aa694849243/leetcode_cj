# -*- coding: utf-8 -*-
import itertools
from typing import List


# 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
#
#  每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
#
#  找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。
#
#
#
#  示例 1：
#
#  输入：stones = [3,2,4,1], K = 2
# 输出：20
# 解释：
# 从 [3, 2, 4, 1] 开始。
# 合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
# 合并 [4, 1]，成本为 5，剩下 [5, 5]。
# 合并 [5, 5]，成本为 10，剩下 [10]。
# 总成本 20，这是可能的最小值。
#
#
#  示例 2：
#
#  输入：stones = [3,2,4,1], K = 3
# 输出：-1
# 解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
#
#
#  示例 3：
#
#  输入：stones = [3,5,1,2,6], K = 3
# 输出：25
# 解释：
# 从 [3, 5, 1, 2, 6] 开始。
# 合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
# 合并 [3, 8, 6]，成本为 17，剩下 [17]。
# 总成本 25，这是可能的最小值。
#
#
#
#
#  提示：
#
#
#  1 <= stones.length <= 30
#  2 <= K <= 30
#  1 <= stones[i] <= 100
#
#  Related Topics 动态规划
#  👍 136 👎 0

# 区间动态规划
# 区间化为点考虑
# https://leetcode-cn.com/problems/minimum-cost-to-merge-stones/solution/qu-jian-dp-by-skyhood/
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        prefix = [0] + [*itertools.accumulate(stones)]
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        dp = [[0] * n for _ in range(n)]
        for delta in range(k - 1, n):
            for i in range(n - delta):
                a = [dp[i][x] + dp[x + 1][i + delta] for x in range(i, i + delta, k - 1)]
                dp[i][i + delta] = (min(a) if a else 0) + (prefix[i + delta + 1] - prefix[i] if delta % (k - 1) == 0 else 0)
        return dp[0][n - 1]


Solution().mergeStones(stones=[3, 5, 1, 2, 6, 9, 12, 23, 7], k=5)
