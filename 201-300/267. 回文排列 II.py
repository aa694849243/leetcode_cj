# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。
#
#  如不能形成任何回文排列时，则返回一个空列表。
#
#  示例 1：
#
#  输入: "aabb"
# 输出: ["abba", "baab"]
#
#  示例 2：
#
#  输入: "abc"
# 输出: []
#  Related Topics 哈希表 字符串 回溯 👍 75 👎 0


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        m = collections.Counter(s)
        cnt = 1
        flag = ''
        cand = ''
        for ch in m:
            if m[ch] % 2:
                cnt -= 1
                if cnt < 0:
                    return []
                flag = ch
            cand += ch * (m[ch] // 2)
        res = set()
        for wlst in itertools.permutations(cand, len(cand)):
            res.add(''.join(wlst))
        ans = []
        for w in res:
            ans.append(w+flag+w[::-1])
        return ans
