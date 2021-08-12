#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR)
#  符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。
#
#  示例 1:
#
#  输入: s = "1^0|0|1", result = 0
#
# 输出: 2
# 解释: 两种可能的括号方法是
# 1^(0|(0|1))
# 1^((0|0)|1)
#
#
#  示例 2:
#
#  输入: s = "0&0&0&1^1|0", result = 1
#
# 输出: 10
#
#  提示：
#
#
#  运算符的数量不超过 19 个
#
#  Related Topics 记忆化搜索 字符串 动态规划
#  👍 46 👎 0
import functools

# 字符串与或问题
class Solution:
    def countEval(self, s: str, result: int) -> int:
        ops = {'&': {1: [(1, 1)], 0: [(1, 0), (0, 0), (0, 1)]},
               '|': {1: [(1, 1), (0, 1), (1, 0)], 0: [(0, 0)]},
               '^': {1: [(0, 1), (1, 0)], 0: [(1, 1), (0, 0)]}}
        @functools.lru_cache(None)
        def dfs(s, target):
            if len(s) == 1:
                return int(int(s) == target)
            ans = 0
            for i, ch in enumerate(s):
                if ch in ops:
                    for l, r in ops[ch][target]:
                        ans += dfs(s[:i], l)*dfs(s[i+1:],r)
            return ans
        return dfs(s,result)