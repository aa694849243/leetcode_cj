#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
#
#  表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分。
#
#  示例 1:
#
#  输入: "3+2*2"
# 输出: 7
#
#
#  示例 2:
#
#  输入: " 3/2 "
# 输出: 1
#
#  示例 3:
#
#  输入: " 3+5 / 2 "
# 输出: 5
#
#
#  说明：
#
#
#  你可以假设所给定的表达式都是有效的。
#  请不要使用内置的库函数 eval。
#
#  Related Topics 栈 数学 字符串
#  👍 50 👎 0


class Solution:
    def calculate(self, s: str) -> int:
        stack_op = []
        stack_num = []
        tmp = ''
        for i in range(len(s)):
            if s[i]==' ':
                continue
            if s[i].isdigit():
                tmp += s[i]
            else:
                if stack_op and stack_op[-1] in '*/':
                    a = stack_num.pop()
                    op = stack_op.pop()
                    if op == '*':
                        tmp = str(int(a) * int(tmp))
                    elif op == '/':
                        tmp = str(int(a) // int(tmp))
                stack_num.append(tmp)
                tmp = ''
                stack_op.append(s[i])
        if stack_op and stack_op[-1] in '*/':
            a = stack_num.pop()
            op = stack_op.pop()
            if op == '*':
                tmp = str(int(a) * int(tmp))
            elif op == '/':
                tmp = str(int(a) // int(tmp))
        stack_num.append(tmp)
        ans = int(stack_num[0])
        for i, val in enumerate(stack_num[1:]):
            if stack_op[i] == '+':
                ans += int(val)
            else:
                ans -= int(val)
        return ans
Solution().calculate("4/3+2")
