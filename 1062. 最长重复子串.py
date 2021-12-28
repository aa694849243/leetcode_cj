#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定字符串 S，找出最长重复子串的长度。如果不存在重复子串就返回 0。
#
#
#
#  示例 1：
#
#  输入："abcd"
# 输出：0
# 解释：没有重复子串。
#
#
#  示例 2：
#
#  输入："abbaba"
# 输出：2
# 解释：最长的重复子串为 "ab" 和 "ba"，每个出现 2 次。
#
#
#  示例 3：
#
#  输入："aabcaabdaab"
# 输出：3
# 解释：最长的重复子串为 "aab"，出现 3 次。
#
#
#  示例 4：
#
#  输入："aaaaa"
# 输出：4
# 解释：最长的重复子串为 "aaaa"，出现 2 次。
#
#
#
#  提示：
#
#
#  字符串 S 仅包含从 'a' 到 'z' 的小写英文字母。
#  1 <= S.length <= 1500
#
#  Related Topics 字符串 二分查找 动态规划 后缀数组 哈希函数 滚动哈希
#  👍 63 👎 0


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        base, mode = 113, 10 ** 9 + 13

        def rabincarp(s, size):
            mult = pow(base, size - 1, mode)
            m = set()
            hash = 0
            for i in range(size):
                hash = (hash * base + ord(s[i])) % mode
            m.add(hash)
            for i in range(size, len(s)):
                hash = ((hash - ord(s[i - size]) * mult) * base + ord(s[i])) % mode
                if hash in m:
                    return True
                m.add(hash)
            return False

        if len(set(s)) == len(s):
            return 0
        l, r = 1, len(s) + 1
        while l < r:
            mid = (l + r) // 2
            if not rabincarp(s, mid):
                r = mid
            else:
                l = mid + 1
        return l if rabincarp(s, l) else l - 1


Solution().longestRepeatingSubstring( "caaabaa")
