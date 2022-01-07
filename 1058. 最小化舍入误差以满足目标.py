# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一系列价格 [p1,p2...,pn] 和一个目标 target，将每个价格 pi 舍入为 Roundi(pi) 以使得舍入数组 [Round1(p1)
# ,Round2(p2)...,Roundn(pn)] 之和达到给定的目标值 target。每次舍入操作 Roundi(pi) 可以是向下舍 Floor(pi)
# 也可以是向上入 Ceil(pi)。
#
#  如果舍入数组之和无论如何都无法达到目标值 target，就返回 -1。否则，以保留到小数点后三位的字符串格式返回最小的舍入误差，其定义为 Σ |
# Roundi(pi) - (pi)|（ i 从 1 到 n ）。
#
#
#
#  示例 1：
#
#  输入：prices = ["0.700","2.800","4.900"], target = 8
# 输出："1.000"
# 解释：
# 使用 Floor，Ceil 和 Ceil 操作得到 (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1
# = 1.0 。
#
#
#  示例 2：
#
#  输入：prices = ["1.500","2.500","3.500"], target = 10
# 输出："-1"
# 解释：
# 达到目标是不可能的。
#
#
#
#  提示：
#
#
#  1 <= prices.length <= 500
#  表示价格的每个字符串 prices[i] 都代表一个介于 0 和 1000 之间的实数，并且正好有 3 个小数位。
#  target 介于 0 和 1000000 之间。
#
#  Related Topics 贪心 数组 数学 字符串 👍 30 👎 0


class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        prices_ = [float(i) for i in prices]
        prices = []
        for i, price in enumerate(prices_):
            if price == int(price):
                target -= price
            else:
                prices.append(price)
        if not prices:
            if target==0:
                return '0.000'
            else:
                return  '-1'
        mi = sum((lmi := list(map(lambda x: int(float(x)), prices))))
        ma = sum((lma := list(map(lambda x: int(float(x)) + 1, prices))))
        if target < mi or target > ma:
            return '-1'
        costs = sorted(f + c - 2 * p for p, f, c in zip(prices, lmi, lma))
        res = sum(prices) - mi + sum(costs[:target - mi])
        return f'{res:.3f}'


Solution().minimizeError(["2.000","2.000","2.000","2.000","2.000"], 10)
