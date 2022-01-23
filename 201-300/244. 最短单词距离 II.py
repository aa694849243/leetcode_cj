#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.m = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.m[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        li1 = self.m[word1]
        li2 = self.m[word2]
        res=float('inf')
        for i in li1:
            for j in li2:
                res=min(abs(i-j),res)
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
