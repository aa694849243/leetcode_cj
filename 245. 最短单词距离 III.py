#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bisect
import collections
from typing import List


# 给定一个字符串数组 wordsDict 和两个字符串 word1 和 word2 ，返回列表中这两个单词之间的最短距离。
#
#  注意：word1 和 word2 是有可能相同的，并且它们将分别表示为列表中 两个独立的单词 。
#
#
#
#  示例 1：
#
#
# 输入：wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "m
# akes", word2 = "coding"
# 输出：1
#
#
#  示例 2：
#
#
# 输入：wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "m
# akes", word2 = "makes"
# 输出：3
#
#
#
#
#  提示：
#
#
#  1 <= wordsDict.length <= 105
#  1 <= wordsDict[i].length <= 10
#  wordsDict[i] 由小写英文字母组成
#  word1 和 word2 都在 wordsDict 中
#
#  Related Topics 数组 字符串
#  👍 40 👎 0

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        m = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            m[w].append(i)
        if word1 == word2:
            li = m[word1]
            res = min(li[i] - li[i - 1] for i in range(1, len(li)))
            return res
        lst1 = m[word1]
        lst2 = m[word2]
        res = float('inf')
        for num in lst2:
            index = bisect.bisect_right(lst1, num)
            if index == 0:
                res = min(res, lst1[index] - num)
            elif index == len(lst1):
                res = min(res, num - lst1[-1])
            else:
                res = min(res, num - lst1[index - 1], lst1[index] - num)
        return res
