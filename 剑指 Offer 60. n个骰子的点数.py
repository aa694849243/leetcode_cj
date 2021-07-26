#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
#
#
#
#  你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
#
#
#
#  示例 1:
#
#  输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
#
#
#  示例 2:
#
#  输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0
# .05556,0.02778]
#
#
#
#  限制：
#
#  1 <= n <= 11
#  Related Topics 数学 动态规划 概率与统计
#  👍 265 👎 0


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = {i: 1 / 6 for i in range(1, 7)}
        for _ in range(n-1):
            ndp = collections.defaultdict(int)
            for i in dp:
                for j in range(1, 7):
                    ndp[i + j] += dp[i] * (1 / 6)
            dp = ndp
        li = sorted(dp)
        return [dp[i] for i in li]
Solution().dicesProbability(2)
