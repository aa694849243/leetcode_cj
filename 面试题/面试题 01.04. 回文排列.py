#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


# 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
#
#  回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
#
#  回文串不一定是字典当中的单词。
#
#
#
#  示例1：
#
#  输入："tactcoa"
# 输出：true（排列有"tacocat"、"atcocta"，等等）
#
#
#
#  Related Topics 位运算 哈希表 字符串
#  👍 54 👎 0


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = collections.Counter(s)
        flag = 1
        for ch in m:
            if m[ch] % 2:
                flag -= 1
                if flag < 0:
                    return False
        return True