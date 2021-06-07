# -*- coding: utf-8 -*-
# 给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。
#
#  返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）
#
#
#
#  示例 1：
#
#  输入："banana"
# 输出："ana"
#
#
#  示例 2：
#
#  输入："abcd"
# 输出：""
#
#
#
#
#  提示：
#
#
#  2 <= S.length <= 10^5
#  S 由小写英文字母组成。
#
#  Related Topics 哈希表 二分查找
#  👍 123 👎 0

# 二分+Rabin-carp
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        base, mod = 119, 10 ** 9 + 9
        n = len(s)

        def solve(l):
            hash = 0
            m = {}
            for i in range(l):
                hash = (hash * base + ord(s[i])) % mod
            m[hash] = s[:l]
            mult = pow(base, l - 1, mod)
            for i in range(l, n):
                hash = ((hash - ord(s[i - l]) * mult) * base + ord(s[i])) % mod
                if hash in m:
                    if m[hash] == s[i - l + 1:i + 1]:
                        return s[i-l+1:i+1]
                else:
                    m[hash] = s[i - l + 1:i + 1]
            return ''

        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if solve(mid):
                l = mid + 1
            else:
                r = mid
        return solve(l-1)
Solution().longestDupSubstring("aaaa")