#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，
# 你能对此优化吗?
#
#  示例：
#
#  输入：words = ["I","am","a","student","from","a","university","in","a","city"],
# word1 = "a", word2 = "student"
# 输出：1
#
#  提示：
#
#
#  words.length <= 100000
#
#  Related Topics 数组 字符串
#  👍 30 👎 0

# 拓展方法可以用哈希表+双指针
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        s, t = [], []
        distance = float('inf')
        for i, word in enumerate(words):
            if word == word1:
                s.append(i)
                if t:
                    distance = min(distance, i - t[-1])
            if word == word2:
                t.append(i)
                if s:
                    distance = min(distance, i - s[-1])
        return distance


# 双指针
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        s, t = [], []
        distance = float('inf')
        for i, word in enumerate(words):
            if word == word1:
                s.append(i)
            if word == word2:
                t.append(i)
        l, r = 0, 0
        while l < len(s) and r < len(t):
            distance = min(distance, abs(s[l] - t[r]))
            if s[l] > t[r]:
                r += 1
            else:
                l += 1
        return distance
