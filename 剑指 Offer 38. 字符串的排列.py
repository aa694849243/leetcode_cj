#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#
#
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#
#
#  示例:
#
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#
#
#
#
#  限制：
#
#  1 <= s 的长度 <= 8
#  Related Topics 字符串 回溯
#  👍 382 👎 0


class Solution:
    def permutation(self, s: str) -> List[str]:
        self.ans = set()

        def dfs(cum, s):
            if not s:
                self.ans.add(cum)
            for i, ch in enumerate(s):
                dfs(cum + ch, s[:i] + s[i + 1:])
        dfs('',s)
        return list(self.ans)
Solution().permutation('abc')