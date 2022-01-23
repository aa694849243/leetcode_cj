#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
#
#  写一个函数来计算范围在 [low, high] 之间中心对称数的个数。
#
#  示例:
#
#  输入: low = "50", high = "100"
# 输出: 3
# 解释: 69，88 和 96 是三个在该范围内的中心对称数
#
#  注意:
# 由于范围可能很大，所以 low 和 high 都用字符串表示。
#  Related Topics 递归 数组 字符串
#  👍 42 👎 0


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def dfs(x):
            if x == 0:
                return ['']
            if x == 1:
                return ['0', '1', '8']
            li = [['1', '1'], ['8', '8'], ['6', '9'], ['9', '6']]
            res = []
            for a, b in li:
                for r in dfs(x - 2):
                    res.append(a + r + b)
            if x != n:
                for r in dfs(x - 2):
                    res.append('0' + r + '0')
            return res

        n1 = min(len(low), len(high))
        n2 = max(len(low), len(high))
        res = 0
        for n in range(n1, n2 + 1):
            for s in dfs(n):
                if int(low) <= int(s) <= int(high):
                    res += 1
        return res
