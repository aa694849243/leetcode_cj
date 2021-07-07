# -*- coding: utf-8 -*-
# 给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。
#
#
#
#  请你生成一个具有下述属性的数组 arr ：
#
#
#  arr 中有 n 个整数。
#  1 <= arr[i] <= m 其中 (0 <= i < n) 。
#  将上面提到的算法应用于 arr ，search_cost 的值等于 k 。
#
#
#  返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。
#
#
#
#  示例 1：
#
#  输入：n = 2, m = 3, k = 1
# 输出：6
# 解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
#
#
#  示例 2：
#
#  输入：n = 5, m = 2, k = 3
# 输出：0
# 解释：没有数组可以满足上述条件
#
#
#  示例 3：
#
#  输入：n = 9, m = 1, k = 1
# 输出：1
# 解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]
#
#
#  示例 4：
#
#  输入：n = 50, m = 100, k = 25
# 输出：34549172
# 解释：不要忘了对 1000000007 取余
#
#
#  示例 5：
#
#  输入：n = 37, m = 17, k = 7
# 输出：418930126
#
#
#
#
#  提示：
#
#
#  1 <= n <= 50
#  1 <= m <= 100
#  0 <= k <= n
#
#  Related Topics 动态规划
#  👍 62 👎 0
import functools


# https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/solution/sheng-cheng-shu-zu-by-leetcode-solution-yswf/
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def f(max_, cost, i):
            if i + 1 < cost:  # 字符的数量少于搜索次数，这是不可能的
                return 0
            if max_ < cost:  # 最大值小于搜索次数，这是不可能的
                return 0
            if cost == 0:  # 没了搜索次数了，找第一个数搜索次数就是1，所以返回0
                return 0
            if i == 0:  # 第一个数搜索次数为1
                return 1
            ans = 0
            ans += max_ * f(max_, cost, i - 1)  # 最后一个不增加搜索次数
            for max__ in range(max_ - 1, 0, -1):
                ans += f(max__, cost - 1, i - 1)  # 最后一个增加搜索次数
            return ans % mod

        return sum(f(j, k, n - 1) for j in range(1, m + 1)) % mod


# 2优化 前缀和

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        if k == 0:
            return 0
        dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]
        for j in range(1, m + 1):
            dp[1][1][j] = 1  # 长度为1，代价为1，最大值为任何数结果都是1
        for i in range(2, n + 1):
            for cost in range(1, k + 1):
                prefix = 0
                for j in range(1, m + 1):
                    dp[i][cost][j] = (dp[i - 1][cost][j] * j + prefix) % mod
                    prefix += dp[i - 1][cost - 1][j]
        return sum(dp[-1][k][j] for j in range(1, m + 1)) % mod


Solution().numOfArrays(n=2, m=3, k=1)
