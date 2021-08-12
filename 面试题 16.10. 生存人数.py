#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定 N 个人的出生年份和死亡年份，第 i 个人的出生年份为 birth[i]，死亡年份为 death[i]，实现一个方法以计算生存人数最多的年份。
#
#  你可以假设所有人都出生于 1900 年至 2000 年（含 1900 和 2000 ）之间。如果一个人在某一年的任意时期处于生存状态，那么他应该被纳入那一
# 年的统计中。例如，生于 1908 年、死于 1909 年的人应当被列入 1908 年和 1909 年的计数。
#
#  如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。
#
#
#
#  示例：
#
#
# 输入：
# birth = {1900, 1901, 1950}
# death = {1948, 1951, 2000}
# 输出： 1901
#
#
#
#
#  提示：
#
#
#  0 < birth.length == death.length <= 10000
#  birth[i] <= death[i]
#
#  Related Topics 数组 计数
#  👍 37 👎 0


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        n = len(birth)
        li = [0] * 102
        for i in range(n):
            a, b = birth[i] - 1900, death[i] - 1900
            li[a] += 1
            li[b+1] -= 1
        ma, my = 0, 1900
        cnt = 0
        for i, val in enumerate(li):
            cnt += val
            if cnt > ma:
                ma, my = cnt, i + 1900
        return my
Solution().maxAliveYear([1928,1958,1902,1953,1912,1923,1937,1915,1942,1964,1954,1924,1936,1963,1950,1904,1931,1951,1953,1922,1970,1986,1947,1911,1913],[1986,1997,1937,1971,1982,1980,1992,1995,1992,1991,1964,1985,1938,1975,1964,1975,1961,1995,1985,1946,1989,1999,1994,1956,1999])