#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符
# 合要求的单词则返回空字符串。
#
#  示例：
#
#  输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
# 输出： "dogwalker"
# 解释： "dogwalker"可由"dog"和"walker"组成。
#
#
#  提示：
#
#
#  0 <= len(words) <= 200
#  1 <= len(words[i]) <= 100
#
#  Related Topics 字典树 数组 哈希表 字符串
#  👍 27 👎 0

class Trie:
    def __init__(self):
        self.lookup = {}

    def insert(self, word):
        tree = self.lookup
        for i in word:
            if i not in tree:
                tree[i] = {}
            tree = tree[i]
        tree['#'] = word

    def search(self, word):
        tree = self.lookup
        for ch in word:
            if ch not in tree:
                return False
            tree = tree[ch]
        return '#' in tree


class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        words.sort(key=lambda x: (-len(x), x))

        def check(word, flag):
            if not word:
                return True
            n = len(word)
            for i in range(1, n + flag):
                if t.search(word[:i]):
                    if check(word[i:],1):
                        return True
            return False

        for word in words:
            if check(word, 0):
                return word
        return ''


Solution().longestWord(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"])
