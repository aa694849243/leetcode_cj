#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
#
#  示例 1：
#
#  输入: s = "leetcode"
# 输出: false
#
#
#  示例 2：
#
#  输入: s = "abc"
# 输出: true
#
#
#  限制：
#
#  0 <= len(s) <= 100
#  如果你不使用额外的数据结构，会很加分。
#
#  Related Topics 位运算 哈希表 字符串 排序
#  👍 132 👎 0


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)


class Solution:
    def isUnique(self, astr: str) -> bool:
        mask = 0
        for ch in astr:
            num = ord(ch) - 97
            if mask & (1 << num):
                return False
            mask|=(1<<num)
        return True
