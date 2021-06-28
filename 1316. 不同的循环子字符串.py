# -*- coding: utf-8 -*-
# 给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目：
#
#
#  可以写成某个字符串与其自身相连接的形式（即，可以写为 a + a，其中 a 是某个字符串）。
#
#
#  例如，abcabc 就是 abc 和它自身连接形成的。
#
#
#
#  示例 1：
#
#  输入：text = "abcabcabc"
# 输出：3
# 解释：3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。
#
#
#  示例 2：
#
#  输入：text = "leetcodeleetcode"
# 输出：2
# 解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。
#
#
#
#
#  提示：
#
#
#  1 <= text.length <= 2000
#  text 只包含小写英文字母。
#
#  Related Topics 字典树 字符串 动态规划 滑动窗口 哈希函数 滚动哈希
#  👍 27 👎 0

# 前缀和rabin-karp
import collections


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        base, mod = 113, 10 ** 9 + 9  # base值和模
        n = len(text)
        m = collections.defaultdict(set)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = (prefix[i - 1] * base + ord(text[i - 1])) % mod

        def mult(leng):
            return pow(base, leng, mod)

        mul = [0] * (n + 1)
        for leng in range(n + 1):
            mul[leng] = mult(leng)

        def hash(l, r):
            return (prefix[r + 1] - prefix[l] * mul[r - l + 1]) % mod

        ans = 0
        for l in range(n):  # 左端点
            for r in range(l, n):  # 第一个右端点
                l1, r1 = l, r
                l2, r2 = r + 1, 2 * r - l + 1
                if r2 < n:
                    hash1 = hash(l1, r1)
                    if hash1 not in m[r - l] and hash1 == hash(l2, r2):  # 每个长度都作一个哈希值集合，减少冲突
                        m[r - l].add(hash1)
                        ans += 1
        return ans


Solution().distinctEchoSubstrings("abcabcabc")
