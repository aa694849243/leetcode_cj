# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一个回文字符串 palindrome ，请你将其中 一个 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。
#
#  请你返回结果字符串。如果无法做到，则返回一个空串。
#
#
#
#  示例 1：
#
#  输入：palindrome = "abccba"
# 输出："aaccba"
#
#
#  示例 2：
#
#  输入：palindrome = "a"
# 输出：""
#
#
#
#
#  提示：
#
#
#  1 <= palindrome.length <= 1000
#  palindrome 只包含小写英文字母。
#
#  Related Topics 贪心 字符串
#  👍 24 👎 0


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<=1:
            return ''
        for i, ch, in enumerate(palindrome):
            if len(palindrome)%2 and i==len(palindrome)//2:
                continue
            if ch=='a':
                continue
            nch='a'
            ns=palindrome[:i]+nch+palindrome[i+1:]
            return ns
        return palindrome[:-1]+'b' #全是a的情况
