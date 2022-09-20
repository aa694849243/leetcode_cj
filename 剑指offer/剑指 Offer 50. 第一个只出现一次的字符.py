#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
#
#  示例:
#
#  s = "abaccdeff"
# 返回 "b"
#
# s = ""
# 返回 " "
#
#
#
#
#  限制：
#
#  0 <= s 的长度 <= 50000
#  Related Topics 队列 哈希表 字符串 计数
#  👍 117 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> str:
        m = [0] * 26
        l = 0
        for i, ch in enumerate(s):
            num = ord(ch) - 97
            m[num] += 1
            while l < len(s) and m[ord(s[l]) - 97] > 1:
                l += 1
        return s[l] if l < len(s) else ' '
