# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
#
#  找到所有长度为 n 的中心对称数。
#
#  示例 :
#
#  输入:  n = 2
# 输出: ["11","69","88","96"]
#
#  Related Topics 递归 数组 字符串 👍 70 👎 0

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        lst = ['' for _ in range(n)]
        lim = (n - 1) // 2

        def dfs(i):
            if i == lim:
                if i != n - 1 - i:
                    for num in '018':
                        lst[i], lst[n - 1 - i] = num, num
                        if lst[0] != '0':
                            res.append(''.join(lst))
                    lst[i], lst[n - 1 - i] = '9', '6'
                    if lst[0] != '0':
                        res.append(''.join(lst))
                    lst[i], lst[n - 1 - i] = '6', '9'
                    if lst[0] != '0':
                        res.append(''.join(lst))
                else:
                    for num in '018':
                        lst[i] = num
                        if lst[0] != '0' or n == 1:
                            res.append(''.join(lst))
                lst[i] = ''
                lst[n - 1 - i] = ''
            else:
                for num in '018':
                    lst[i], lst[n - 1 - i] = num, num
                    dfs(i + 1)
                    lst[i], lst[n - 1 - i] = '', ''
                lst[i], lst[n - 1 - i] = '6', '9'
                dfs(i + 1)
                lst[i], lst[n - 1 - i] = '9', '6'
                dfs(i + 1)
                lst[i], lst[n - 1 - i] = '', ''

        dfs(0)
        return res


Solution().findStrobogrammatic(4)
