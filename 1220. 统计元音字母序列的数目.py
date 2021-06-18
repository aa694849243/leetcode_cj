# -*- coding: utf-8 -*-


# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
#
#
#  字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
#  每个元音 'a' 后面都只能跟着 'e'
#  每个元音 'e' 后面只能跟着 'a' 或者是 'i'
#  每个元音 'i' 后面 不能 再跟着另一个 'i'
#  每个元音 'o' 后面只能跟着 'i' 或者是 'u'
#  每个元音 'u' 后面只能跟着 'a'
#
#
#  由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
#
#
#
#  示例 1：
#
#  输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
#
#
#  示例 2：
#
#  输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
#
#
#  示例 3：
#
#  输入：n = 5
# 输出：68
#
#
#
#  提示：
#
#
#  1 <= n <= 2 * 10^4
#
#  Related Topics 动态规划
#  👍 33 👎 0
import functools


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(ch, n):
            if n == 0:
                return 1
            a = 0
            if ch == 'a':
                a += dp('u', n - 1) + dp('i', n - 1) + dp('e', n - 1)
            elif ch == 'e':
                a += dp('a', n - 1) + dp('i', n - 1)
            elif ch == 'i':
                a += dp('e', n - 1) + dp('o', n - 1)
            elif ch == 'o':
                a += dp('i', n - 1)
            else:
                a += dp('i', n - 1) + dp('o', n - 1)
            return a % mod

        ans = 0
        for ch in 'aeiou':
            ans += dp(ch, n - 1)
        return ans % mod


Solution().countVowelPermutation(5)
