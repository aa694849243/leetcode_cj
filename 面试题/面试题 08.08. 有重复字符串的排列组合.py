#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
#
#  示例1:
#
#   输入：S = "qqe"
#  输出：["eqq","qeq","qqe"]
#
#
#  示例2:
#
#   输入：S = "ab"
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
#  👍 41 👎 0


class Solution:
    def permutation(self, S: str) -> List[str]:
        S = sorted(S)
        res = []

        def dfs(s, paths):
            if not s:
                res.append(''.join(paths))
            for i, ch in enumerate(s):
                if i > 0 and ch == s[i - 1]:
                    continue
                dfs(s[:i] + s[i + 1:], paths + [ch])

        dfs(S, [])
        return res
