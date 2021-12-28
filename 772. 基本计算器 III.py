#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现一个基本的计算器来计算简单的表达式字符串。
#
#  表达式字符串只包含非负整数，算符 +、-、*、/ ，左括号 ( 和右括号 ) 。整数除法需要 向下截断 。
#
#  你可以假定给定的表达式总是有效的。所有的中间结果的范围为 [-231, 231 - 1] 。
#
#
#
#  示例 1：
#
#
# 输入：s = "1+1"
# 输出：2
#
#
#  示例 2：
#
#
# 输入：s = "6-4/2"
# 输出：4
#
#
#  示例 3：
#
#
# 输入：s = "2*(5+5*2)/3+(6/2+8)"
# 输出：21
#
#
#  示例 4：
#
#
# 输入：s = "(2+6*3+5-(3*14/7+2)*5)+3"
# 输出：-12
#
#
#  示例 5：
#
#
# 输入：s = "0"
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= s <= 104
#  s 由整数、'+'、'-'、'*'、'/'、'(' 和 ')' 组成
#  s 是一个 有效的 表达式
#
#
#
#
#  进阶：你可以在不使用内置库函数的情况下解决此问题吗？
#  Related Topics 栈 递归 数学 字符串
#  👍 100 👎 0


class Solution:
    def calculate(self, s: str) -> int:
        stnum = []
        stopt = []
        pr = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}

        def cal(a, b, opt):
            if opt == '+':
                return a + b
            elif opt == '-':
                return a - b
            elif opt == '*':
                return a * b
            else:
                return int(int(a) / int(b))

        i = 0
        while i < (n := len(s)):
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isdigit():
                j = i
                num_ = 0
                while j < n and s[j].isdigit():
                    num_ = num_ * 10 + int(s[j])
                    j += 1
                i = j - 1
                stnum.append(num_)
            elif s[i] == '(':
                stopt.append('(')
            elif s[i] == ')':
                a = stnum.pop()
                while stopt[-1] != '(':
                    b = stnum.pop()
                    opt = stopt.pop()
                    a = cal(b, a, opt)
                stopt.pop()
                stnum.append(a)
            elif s[i] in '+-*/':
                while stopt and pr[stopt[-1]] >= pr[s[i]]:
                    a, b = stnum.pop(), stnum.pop()
                    nnum = cal(b, a, stopt.pop())
                    stnum.append(nnum)
                stopt.append(s[i])
            i += 1
        while stopt:
            a, b = stnum.pop(), stnum.pop()
            nnum = cal(b, a, stopt.pop())
            stnum.append(nnum)
        return stnum[-1]


Solution().calculate("2*(5+5*2)/3+(6/2+8)")
