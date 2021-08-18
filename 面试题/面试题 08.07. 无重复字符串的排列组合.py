#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。
#
#  示例1:
#
#
#  输入：S = "qwe"
#  输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
#
#
#  示例2:
#
#
#  输入：S = "ab"
#  输出：["ab", "ba"]
#
#
#  提示:
#
#
#  字符都是英文字母。
#  字符串长度在[1, 9]之间。
#
#  Related Topics 字符串 回溯
#  👍 50 👎 0


class Solution:
    def permutation(self, S: str) -> List[str]:
        res = []

        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i, ch in enumerate(s):
                dfs(s[:i] + s[i + 1:], path + ch)
        dfs(S,'')
        return res
