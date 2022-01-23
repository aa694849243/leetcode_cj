# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。
#
#  例如，321 是一个步进数，而 421 不是。
#
#  给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。
#
#
#
#  示例：
#
#  输入：low = 0, high = 21
# 输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]
#
#
#
#
#  提示：
#
#
#  0 <= low <= high <= 2 * 10^9
#
#  Related Topics 广度优先搜索 回溯 👍 30 👎 0


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        t = [*range(1, 10)]
        res = []
        while 1:
            tree = []
            for num in t:
                if low <= num <= high:
                    res.append(num)
                elif num > high:
                    return res if low != 0 else [0] + res
                a = num % 10 + 1
                b = num % 10 - 1
                if b >= 0:
                    tree.append(num * 10 + b)
                if a < 10:
                    tree.append(num * 10 + a)
            t = tree


Solution().countSteppingNumbers(0, 21)
