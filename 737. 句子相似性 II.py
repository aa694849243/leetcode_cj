# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定两个句子 words1, words2 （每个用字符串数组表示），和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。
#
#  例如，当相似单词对是 pairs = [["great", "fine"], ["acting","drama"], ["skills",
# "talent"]]的时候，words1 = ["great", "acting", "skills"] 和 words2 = ["fine", "drama",
# "talent"] 是相似的。
#
#  注意相似关系是 具有 传递性的。例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，则 "great" 和
# "good" 是相似的。
#
#  而且，相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。
#
#  并且，一个单词总是与其自身相似。例如，句子 words1 = ["great"], words2 = ["great"], pairs = [] 是相似的
# ，尽管没有输入特定的相似单词对。
#
#  最后，句子只会在具有相同单词个数的前提下才会相似。所以一个句子 words1 = ["great"] 永远不可能和句子 words2 = [
# "doubleplus","good"] 相似。
#
#  注：
#
#
#  words1 and words2 的长度不会超过 1000。
#  pairs 的长度不会超过 2000。
#  每个pairs[i] 的长度为 2。
#  每个 words[i] 和 pairs[i][j] 的长度范围为 [1, 20]。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 哈希表 字符串 👍 53 👎 0


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                f[b] = a

        for x, y in similarPairs:
            union(x, y)
        for i in range(len(sentence1)):
            a, b = find(sentence1[i]), find(sentence2[i])
            if a!=b:
                return False
        return True
Solution().areSentencesSimilarTwo(["great","acting","skills"], ["fine","drama","talent"],[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]])