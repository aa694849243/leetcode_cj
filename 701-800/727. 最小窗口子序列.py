#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 给定字符串 S and T，找出 S 中最短的（连续）子串 W ，使得 T 是 W 的 子序列 。
#
#  如果 S 中没有窗口可以包含 T 中的所有字符，返回空字符串 ""。如果有不止一个最短长度的窗口，返回开始位置最靠左的那个。
#
#  示例 1：
#
#  输入：
# S = "abcdebdde", T = "bde"
# 输出："bcde"
# 解释：
# "bcde" 是答案，因为它在相同长度的字符串 "bdde" 出现之前。
# "deb" 不是一个更短的答案，因为在窗口中必须按顺序出现 T 中的元素。
#
#
#
#  注：
#
#
#  所有输入的字符串都只包含小写字母。All the strings in the input will only contain lowercase let
# ters.
#  S 长度的范围为 [1, 20000]。
#  T 长度的范围为 [1, 100]。
#
#
#
#  Related Topics 字符串 动态规划 滑动窗口
#  👍 105 👎 0


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        cur = [-1] * len(s1)
        for i, ch in enumerate(s1):
            if ch == s2[0]:
                cur[i] = i
        for ch in s2[1:]:
            last = -1
            new = [-1] * len(s1)
            for j in range(len(s1)):
                if last != -1 and s1[j] == ch:
                    new[j] = last
                if cur[j] != -1:
                    last = cur[j]
            cur = new
        res = float('inf')
        ans = ''
        for i, j in enumerate(cur):
            if j != -1 and i - j < res:
                res = i - j
                ans = s1[j:i + 1]
        return ans


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n = len(s1)
        dp = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            num = ord(s1[i]) - 97
            for j in range(26):
                if j == num:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]
        poses = [i for i in range(n) if s1[i] == s2[0]]
        ans = ''
        for pos in poses:
            st = pos
            pos = pos + 1
            for ch in s2[1:]:
                nxt = dp[pos][ord(ch) - 97]
                if nxt >= n:
                    break
                else:
                    pos = nxt + 1
            else:
                if not ans or pos - st < len(ans):
                    ans = s1[st:pos]
        return ans


Solution().minWindow("abcdebdde", "bde")
