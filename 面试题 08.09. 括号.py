#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。
#
#  说明：解集不能包含重复的子集。
#
#  例如，给出 n = 3，生成结果为：
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#
#  Related Topics 字符串 动态规划 回溯
#  👍 78 👎 0

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(bal, s, left):
            if bal == 0 and left == n:
                res.append(s)
                return
            for ch in '()':
                if bal == 0 and ch == ')':
                    continue
                if left == n and ch == '(':
                    continue
                if ch == '(':
                    dfs(bal + 1, s + ch, left + 1)
                else:
                    dfs(bal - 1, s + ch, left)
        dfs(0,'',0)
        return res
