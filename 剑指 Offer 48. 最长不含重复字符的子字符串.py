#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
#
#
#  示例 1:
#
#  输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
#  提示：
#
#
#  s.length <= 40000
#
#
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-rep
# eating-characters/
#  Related Topics 哈希表 字符串 滑动窗口
#  👍 241 👎 0
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = collections.defaultdict(lambda: -1)
        ans = 0
        l = -1
        for i, ch in enumerate(s):
            if m[ch] == -1:
                ans = max(ans, i - l)
                m[ch] = i
            else:
                l = max(l, m[ch])
                ans = max(ans, i - l)
                m[ch] = i
        return ans


Solution().lengthOfLongestSubstring("")
