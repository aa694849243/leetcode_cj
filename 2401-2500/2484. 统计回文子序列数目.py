# -*- coding: utf-8 -*-
# datetime： 2023-01-27 20:13
# ide： PyCharm
import collections


class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        if n < 5:
            return 0
        mod = 10 ** 9 + 7
        left_1ch = [0] * 10
        left_2ch = [0] * 100
        right_1ch = [0] * 10
        right_2ch = [0] * 100
        for d in map(int, reversed(s)):
            for unit, c in enumerate(right_1ch):
                right_2ch[d * 10 + unit] += c
            right_1ch[d] += 1
        ans = 0
        for d in map(int, s):
            right_1ch[d] -= 1  # 先减后缀再加前缀
            for unit, c in enumerate(right_1ch):
                right_2ch[d * 10 + unit] -= c
            ans += sum(a * b for a, b in zip(left_2ch, right_2ch))
            for unit, c in enumerate(left_1ch):
                left_2ch[d * 10 + unit] += c
            left_1ch[d] += 1
        return ans % mod

# leetcode submit region end(Prohibit modification and deletion)


print(Solution().countPalindromes("103301"))

