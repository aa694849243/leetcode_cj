#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
#
#  注意：本题相对原题稍作修改
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串 排序
#  👍 80 👎 0


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=collections.defaultdict(list)
        for s in strs:
            m[tuple(sorted(s))].append(s)
        res=[]
        for ch in m:
            res.append(m[ch])
        return res