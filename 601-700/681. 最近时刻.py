# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个形如 “HH:MM” 表示的时刻，利用当前出现过的数字构造下一个距离当前时间最近的时刻。每个出现数字都可以被无限次使用。
#
#  你可以认为给定的字符串一定是合法的。例如，“01:34” 和 “12:09” 是合法的，“1:34” 和 “12:9” 是不合法的。
#
#
#
#  样例 1:
#
#  输入: "19:34"
# 输出: "19:39"
# 解释: 利用数字 1, 9, 3, 4 构造出来的最近时刻是 19:39，是 5 分钟之后。结果不是 19:33 因为这个时刻是 23 小时 59 分钟之后
# 。
#
#
#
#
#  样例 2:
#
#  输入: "23:59"
# 输出: "22:22"
# 解释: 利用数字 2, 3, 5, 9 构造出来的最近时刻是 22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻。
#
#
#
#  Related Topics 字符串 枚举 👍 57 👎 0


class Solution:
    def nextClosestTime(self, time: str) -> str:
        cand = set()
        for ch in time:
            if ch != ':':
                cand.add(ch)
        cand = list(cand)
        cand2 = set()
        if len(cand)==1:
            return time
        def dfs(lst):
            if len(lst) == 4:
                cand2.add(''.join(lst))
                return
            for ch in cand:
                dfs(lst + [ch])

        dfs([])
        h = int(time[:2])
        m = int(time[-2:])
        delta = float('inf')
        res = ''
        for w in cand2:
            h_ = int(w[:2])
            m_ = int(w[2:])
            if h_==h and m_==m:
                continue
            if h_ >= 24 or m_ >= 60:
                continue
            if h > h_:
                if m_ >= m:
                    x = (h_ + 24 - h) * 60 + (m_ - m)
                else:
                    x = (h_ + 23 - h) * 60 + (m_ + 60 - m)
            elif h < h_:
                if m_ >= m:
                    x = (h_ - h) * 60 + (m_ - m)
                else:
                    x = (h_ - h - 1) * 60 + (m_ + 60 - m)
            else:
                if m_ >= m:
                    x = m_ - m
                else:
                    x = 23 * 60 + 60 + m_ - m
            if x < delta:
                delta = x
                res =w[:2]+':'+w[2:]
        return res


Solution().nextClosestTime("19:34")
