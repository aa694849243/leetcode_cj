#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 绘制直线。有个单色屏幕存储在一个一维数组中，使得32个连续像素可以存放在一个 int 里。屏幕宽度为w，且w可被32整除（即一个 int 不会分布在两行上）
# ，屏幕高度可由数组长度及屏幕宽度推算得出。请实现一个函数，绘制从点(x1, y)到点(x2, y)的水平线。
#
#  给出数组的长度 length，宽度 w（以比特为单位）、直线开始位置 x1（比特为单位）、直线结束位置 x2（比特为单位）、直线所在行数 y。返回绘制过后
# 的数组。
#
#  示例1:
#
#   输入：length = 1, w = 32, x1 = 30, x2 = 31, y = 0
#  输出：[3]
#  说明：在第0行的第30位到第31为画一条直线，屏幕表示为[0b000000000000000000000000000000011]
#
#
#  示例2:
#
#   输入：length = 3, w = 96, x1 = 0, x2 = 95, y = 0
#  输出：[-1, -1, -1]
#
#  Related Topics 位运算 数组 数学
#  👍 12 👎 0


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        def cal(num):
            x = 0xffffffff
            return num if num <= 0x7fffffff else ~(num ^ x)

        cnt = w // 32
        ans = [0] * cnt
        l = x1 // 32
        r = x2 // 32
        l_ = x1 % 32
        r_ = x2 % 32
        for i in range(cnt):
            num = ['0'] * 32
            if i == l:
                if r == i:
                    num[l_:r_ + 1] = ['1'] * len(num[l_:r_ + 1])
                    ans[l] = cal(int(''.join(num), 2))
                    break
                else:
                    num[l_:] = ['1'] * len(num[l_:])
                    ans[l] = cal(int(''.join(num), 2))
            elif i > l:
                if r == i:
                    num[:r_ + 1] = ['1'] * len(num[:r_ + 1])
                    ans[i] = cal(int(''.join(num), 2))
                    break
                else:
                    ans[i] = -1
        res = [0] * length
        res[y * cnt:y * cnt + cnt] = ans
        return res


Solution().drawLine(3, 96, 0, 95, 0)
