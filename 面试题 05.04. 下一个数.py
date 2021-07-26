#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。
#
#  示例1:
#
#
#  输入：num = 2（或者0b10）
#  输出：[4, 1] 或者（[0b100, 0b1]）
#
#
#  示例2:
#
#
#  输入：num = 1
#  输出：[2, -1]
#
#
#  提示:
#
#
#  num的范围在[1, 2147483647]之间；
#  如果找不到前一个或者后一个满足条件的正数，那么输出 -1。
#
#  Related Topics 位运算
#  👍 30 👎 0


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        if num == 2147483647:
            return [-1, -1]
        s = '0' + str(bin(num))[2:]
        ma, mi = -1, -1
        for i in range(len(s) - 2, -1, -1):
            if s[i] + s[i + 1] == '01' and ma == -1:
                ma = i
            if s[i] + s[i + 1] == '10' and mi == -1:
                mi = i
            if ma != -1 and mi != -1:
                break
        s_ma = int(s[:ma] + '10' + '0' * collections.Counter(s[ma + 2:])['0'] + '1' * collections.Counter(s[ma + 2:])['1'], 2) if ma != -1 else -1
        s_mi = int(s[:mi] + '01' + '1' * collections.Counter(s[mi + 2:])['1'] + '0' * collections.Counter(s[mi + 2:])['0'], 2) if mi != -1 else -1
        return [s_ma, s_mi]


Solution().findClosedNumbers(124)
