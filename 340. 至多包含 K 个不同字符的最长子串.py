# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
#
#
#
#  示例 1:
#
#
# 输入: s = "eceba", k = 2
# 输出: 3
# 解释: 则 T 为 "ece"，所以长度为 3。
#
#  示例 2:
#
#
# 输入: s = "aa", k = 1
# 输出: 2
# 解释: 则 T 为 "aa"，所以长度为 2。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 5 * 10⁴
#  0 <= k <= 50
#
#  Related Topics 哈希表 字符串 滑动窗口 👍 165 👎 0


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k < 1:
            return k
        m = collections.defaultdict(int)
        l = 0
        res = 0
        for i, ch in enumerate(s):
            m[ch] += 1
            if len(m) <= k:
                res = max(res, i - l + 1)
            else:
                while l < i:
                    m[s[l]] -= 1
                    if m[s[l]] == 0:
                        m.pop(s[l])
                    l += 1
                    if len(m) <= k:
                        break
                res = max(res, i - l + 1)
        return res


Solution().lengthOfLongestSubstringKDistinct("ab", 1)
