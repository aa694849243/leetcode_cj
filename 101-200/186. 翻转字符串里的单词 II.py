# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个字符串，逐个翻转字符串中的每个单词。
#
#  示例：
#
#  输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# 输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
#
#  注意：
#
#
#  单词的定义是不包含空格的一系列字符
#  输入字符串中不会包含前置或尾随的空格
#  单词与单词之间永远是以单个空格隔开的
#
#
#  进阶：使用 O(1) 额外空间复杂度的原地解法。
#  Related Topics 双指针 字符串 👍 70 👎 0


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rev(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        n = len(s)
        rev(0, n-1)
        l, r = 0, 0
        while l < n:
            while r < n and s[r] != ' ':
                r += 1
            if r < n and s[r] == ' ':
                rev(l, r - 1)
            elif r == n:
                rev(l, r - 1)
            r += 1
            l = r


Solution().reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"])
