#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。
#
#  示例:
#
#  输入: a = 1, b = 1
# 输出: 2
#
#
#
#  提示：
#
#
#  a, b 均可能是负数或 0
#  结果不会溢出 32 位整数
#
#  Related Topics 位运算 数学
#  👍 48 👎 0


class Solution:
    def add(self, a: int, b: int) -> int:
        def plus(a, b, ans, carry, loc):
            while a or b:
                if a & 1 and b & 1:
                    if carry:
                        ans |= (1 << loc)
                    else:
                        carry = 1
                elif a & 1 or b & 1:
                    if carry:
                        carry = 1
                    else:
                        ans |= (1 << loc)
                else:
                    if carry:
                        ans |= (1 << loc)
                        carry = 0
                a >>= 1
                b >>= 1
                loc = abs(~loc)
            if carry:
                ans |= (1 << loc)
            return ans

        def minus(a, b, ans, carry, loc):
            while a:
                if a & 1 and b & 1:
                    if carry:
                        carry = 1
                        ans |= (1 << loc)
                    else:
                        carry = 0
                elif a & 1:
                    if carry:
                        carry = 0
                    else:
                        ans |= (1 << loc)
                elif b & 1:
                    if carry:
                        carry = 1
                    else:
                        carry = 1
                        ans |= (1 << loc)
                else:
                    if carry:
                        ans |= (1 << loc)
                a >>= 1
                b >>= 1
                loc = abs(~loc)
            return ans

        if abs(a) < abs(b):
            a, b = b, a
        if a >= 0 and b >= 0:
            return plus(a, b, 0, 0, 0)
        elif a >= 0 and b <= 0:
            return minus(a, abs(b), 0, 0, 0)
        elif a <= 0 and b >= 0:
            return -minus(abs(a), b, 0, 0, 0)
        else:
            return -plus(abs(a), abs(b), 0, 0, 0)


# 简洁位运算
class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b != 0:
            sum = a ^ b
            carry = ((a & b) << 1)&0xFFFFFFFF
            a = sum
            b = carry
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


Solution().add(3, 0)
