#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。
#
#  示例1:
#
#
#  输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
#  输出：2
#
#
#  示例2:
#
#
#  输入：A = 1，B = 2
#  输出：2
#
#
#  提示:
#
#
#  A，B范围在[-2147483648, 2147483647]之间
#
#  Related Topics 位运算
#  👍 29 👎 0


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        num = A ^ B
        cnt = 0
        while num:
            num &= (num - 1)
            cnt += 1
        return cnt
