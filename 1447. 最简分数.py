#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于 n 的 最简 分数 。分数可以以 任意 顺序返回。
#
#
#
#  示例 1：
#
#  输入：n = 2
# 输出：["1/2"]
# 解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
#
#  示例 2：
#
#  输入：n = 3
# 输出：["1/2","1/3","2/3"]
#
#
#  示例 3：
#
#  输入：n = 4
# 输出：["1/2","1/3","1/4","2/3","3/4"]
# 解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
#
#  示例 4：
#
#  输入：n = 1
# 输出：[]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 100
#
#  Related Topics 数学
#  👍 12 👎 0


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        res = set()
        for den in range(2, n + 1):
            for f in range(1, den):
                coe = gcd(den, f)
                a, b = f // coe, den // coe
                res.add(str(a)+'/'+str(b))
        return list(res)

