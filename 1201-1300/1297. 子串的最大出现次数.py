# -*- coding: utf-8 -*-
import collections


# 给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：
#
#
#  子串中不同字母的数目必须小于等于 maxLetters 。
#  子串的长度必须大于等于 minSize 且小于等于 maxSize 。
#
#
#
#
#  示例 1：
#
#  输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# 输出：2
# 解释：子串 "aab" 在原字符串中出现了 2 次。
# 它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
#
#
#  示例 2：
#
#  输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# 输出：2
# 解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
#
#
#  示例 3：
#
#  输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# 输出：3
#
#
#  示例 4：
#
#  输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10^5
#  1 <= maxLetters <= 26
#  1 <= minSize <= maxSize <= min(26, s.length)
#  s 只包含小写英文字母。
#
#  Related Topics 位运算 字符串
#  👍 51 👎 0

# 1模拟
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        m = collections.defaultdict(int)
        ans = 0

        for i in range(n := len(s)):
            c = collections.defaultdict(int)
            cur = ''
            for j in range(i, min(i + maxSize, n)):
                cur += s[j]
                c[s[j]] += 1
                if len(c.keys()) > maxLetters:
                    break
                if len(cur) >= minSize:
                    m[cur] += 1
                    if m[cur] > ans:
                        ans = m[cur]
        return ans


# 2优化 某字符串的子串出现次数一定不小于该字符串
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        m = collections.defaultdict(int)
        ans = 0
        n = len(s)
        for i in range(n - minSize + 1):
            cur = s[i:i + minSize]
            dif = len(set(cur))
            if dif <= maxLetters:
                m[cur] += 1
                if m[cur] > ans:
                    ans = m[cur]
        return ans
import itertools

# rabin-karp,滚动哈希 未考虑哈希冲突
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        m = collections.defaultdict(int)
        c = collections.defaultdict(int)
        ans = 0
        n = len(s)
        base, mod = 113, 10 ** 9 + 9
        mult = pow(base, minSize - 1, mod)
        hash = 0
        dif = 0
        for i in range(minSize):
            c[s[i]] += 1
            if c[s[i]] == 1:
                dif += 1
            hash = (hash * base + ord(s[i])) % mod
        if dif <= maxLetters:
            m[hash] += 1
            ans = 1
        for i in range(minSize, n):
            c[s[i - minSize]] -= 1
            if c[s[i - minSize]] == 0:
                dif -= 1
            c[s[i]] += 1
            if c[s[i]] == 1:
                dif += 1
            hash = ((hash - ord(s[i - minSize]) * mult) * base + ord(s[i])) % mod
            if dif <= maxLetters:
                m[hash] += 1
                ans = max(m[hash], ans)
        return ans


Solution().maxFreq("aababcaab", 2, 3, 4)
