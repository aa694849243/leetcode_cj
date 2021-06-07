# -*- coding: utf-8 -*-
import collections


# 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
#
#  注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同
#
#
#
#  示例 1：
#
#
# 输入：s = "bcabc"
# 输出："abc"
#
#
#  示例 2：
#
#
# 输入：s = "cbacdcbc"
# 输出："acdb"
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 由小写英文字母组成
#
#  Related Topics 栈 贪心算法 字符串
#  👍 98 👎 0

# 1栈
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        m = collections.Counter(s)
        m2 = set()
        for i, ch in enumerate(s):
            while stack and ch < stack[-1] and m[stack[-1]] > 1 and ch not in m2:
                a = stack.pop()
                m[a] -= 1
                m2.discard(a)
            if ch not in m2:
                stack.append(ch)
                m2.add(ch)
            else:
                m[ch] -= 1
        return ''.join(stack)


# 2递归
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        pos = 0
        m = collections.Counter(s)
        for i in range(len(s)):
            if s[i] < s[pos]: pos = i
            m[s[i]]-=1
            if m[s[i]]==0:
                break
        return s[pos]+self.smallestSubsequence(s[pos+1:].replace(s[pos],'')) if s else ''

Solution().smallestSubsequence("bcabc")
