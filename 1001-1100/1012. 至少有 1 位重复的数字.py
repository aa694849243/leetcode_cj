# -*- coding: utf-8 -*-
# 给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数的个数。
#
#
#
#  示例 1：
#
#  输入：20
# 输出：1
# 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
#
#
#  示例 2：
#
#  输入：100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
#
#
#  示例 3：
#
#  输入：1000
# 输出：262
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#
#  Related Topics 数学 动态规划
#  👍 84 👎 0

import functools
# 数位dp
#https://leetcode-cn.com/problems/numbers-with-repeated-digits/solution/pai-lie-shu-qiu-jie-by-wzhaooooo/
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(m, n):
            if n == 0:
                return 1
            return (m - n + 1) * dp(m, n - 1)

        a = [int(i) for i in str(n + 1)]  # n+1获得的顶格值为n
        ans = 0
        for i in range(1, len(a)):
            ans += 9 * dp(9, i - 1)
        seen = set()  # 储存顶格值
        for i, num in enumerate(a):
            if i == 0:
                usenumber = num - 1
            else:
                usenumber = len([i for i in range(num) if i not in seen]) #因为取的是range(num)，这个方程取到的最大值为全满顶格数-1，即N
            ans += usenumber * dp(10 - i - 1, len(a) - i - 1)  # 非顶格数，满位置的情况
            if num in seen:  # 将每位的顶格数存储，若其他顶格数与其相同，则不必考虑了
                break
            seen.add(num)
        return n-ans
Solution().numDupDigitsAtMostN(20)