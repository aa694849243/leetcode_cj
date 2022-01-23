# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个近义词表 synonyms 和一个句子 text ， synonyms 表中是一些近义词对 ，你可以将句子 text 中每个单词用它的近义词来替换。
#
#
#  请你找出所有用近义词替换后的句子，按 字典序排序 后返回。
#
#
#
#  示例 1：
#
#
# 输入：
# synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
# text = "I am happy today but was sad yesterday"
# 输出：
# ["I am cheerful today but was sad yesterday",
# "I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]
#
#
#
#
#  提示：
#
#
#  0 <= synonyms.length <= 10
#  synonyms[i].length == 2
#  synonyms[0] != synonyms[1]
#  所有单词仅包含英文字母，且长度最多为 10 。
#  text 最多包含 10 个单词，且单词间用单个空格分隔开。
#
#  Related Topics 并查集 数组 哈希表 字符串 回溯 👍 24 👎 0


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                f[b] = a

        m = collections.defaultdict(list)
        f = {}
        w = set()
        for a, b in synonyms:
            union(a, b)
            w |= {a, b}
        for ch in w:
            m[find(ch)].append(ch)
        li = text.split()
        n = len(li)
        res = []

        def dfs(i, pre):
            if i == n:
                res.append(' '.join(pre))
                return
            w = li[i]
            orgin = find(w)
            if orgin not in m:
                dfs(i + 1, pre + [w])
            else:
                for ch in m[orgin]:
                    dfs(i + 1, pre + [ch])

        dfs(0, [])
        return sorted(res)


Solution().generateSentences([["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]],
                             "I am happy today but was sad yesterday")
