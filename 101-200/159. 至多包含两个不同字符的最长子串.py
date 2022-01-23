#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。
#
#  示例 1:
#
#  输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
#
#
#  示例 2:
#
#  输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。
#
#  Related Topics 哈希表 字符串 滑动窗口
#  👍 142 👎 0


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        m = collections.defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            m[s[r]] += 1
            if len(m) < 3:
                continue
            else:
                res = max(res, r - l)
                while l < r:
                    m[s[l]] -= 1
                    if m[s[l]]==0:
                        m.pop(s[l])
                    l += 1
                    if len(m) < 3:
                        break
        if len(m) < 3:
            res = max(res, len(s) - l)
        return res


Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb")
