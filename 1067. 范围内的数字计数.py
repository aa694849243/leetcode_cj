# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个在 0 到 9 之间的整数 d，和两个正整数 low 和 high 分别作为上下界。返回 d 在 low 和 high 之间的整数中出现的次数，包括
# 边界 low 和 high。
#
#
#
#  示例 1：
#
#  输入：d = 1, low = 1, high = 13
# 输出：6
# 解释：
# 数字 d=1 在 1,10,11,12,13 中出现 6 次。注意 d=1 在数字 11 中出现两次。
#
#
#  示例 2：
#
#  输入：d = 3, low = 100, high = 250
# 输出：35
# 解释：
# 数字 d=3 在 103,113,123,130,131,...,238,239,243 出现 35 次。
#
#
#
#
#  提示：
#
#
#  0 <= d <= 9
#  1 <= low <= high <= 2×10^8
#
#  Related Topics 数学 动态规划 👍 20 👎 0

# 数位dp
# https://leetcode-cn.com/problems/digit-count-in-range/solution/python3dai-ma-zhu-wei-tong-ji-by-trojanmaster/
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        edge = str(low).count(str(d))
        if low == high:
            return edge
        return self.cal(high, str(d)) - self.cal(low, str(d)) + edge

    def cal(self, limit, d):
        w = str(limit)
        res = 0
        for i in range(len(w) - 1, -1, -1):
            if w[i] == d:
                part1 = int(w[:i]) * 10 ** (len(w) - i - 1) if i != 0 else 0  # i左边的数
                part2 = int(w[i + 1:]) + 1 if i != len(w) - 1 else 1  # i右边的数
                res += part1 + part2
            elif int(w[i]) > int(d):
                part1 = (int(w[:i])+1)*10**(len(w)-i-1) if i!=0 else 1
