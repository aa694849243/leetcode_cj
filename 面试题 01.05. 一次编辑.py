#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
#
#
#
#  示例 1:
#
#  输入:
# first = "pale"
# second = "ple"
# 输出: True
#
#
#
#  示例 2:
#
#  输入:
# first = "pales"
# second = "pal"
# 输出: False
#
#  Related Topics 双指针 字符串
#  👍 82 👎 0


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False
        cnt = 1
        if len(first) == len(second):
            for i in range(len(first)):
                if first[i] != second[i]:
                    cnt -= 1
                    if cnt < 0:
                        return False
            return True
        if len(first) < len(second):
            first, second = second, first
        offset = 0
        for i in range(len(first)):
            if i + offset == len(second):
                return offset == 0
            if first[i] != second[i + offset]:
                offset -= 1
                if offset < -1:
                    return False
        return True
Solution().oneEditAway("b",'')