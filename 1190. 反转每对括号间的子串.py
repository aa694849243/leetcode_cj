# -*- coding: utf-8 -*-
# 给出一个字符串 s（仅含有小写英文字母和括号）。
#
#  请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
#
#  注意，您的结果中 不应 包含任何括号。
#
#
#
#  示例 1：
#
#  输入：s = "(abcd)"
# 输出："dcba"
#
#
#  示例 2：
#
#  输入：s = "(u(love)i)"
# 输出："iloveu"
#
#
#  示例 3：
#
#  输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
#
#
#  示例 4：
#
#  输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 2000
#  s 中只有小写英文字母和括号
#  我们确保所有括号都是成对出现的
#
#  Related Topics 栈
#  👍 139 👎 0


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        backets = []
        for i in range(len(s)):
            if s[i] == '(':
                backets.append('(')
                stack.append([])
            elif s[i] == ')':
                backets.pop()
                a = stack.pop()[::-1]
                stack[-1].extend(a)
            else:
                stack[-1].append(s[i])
        return ''.join(stack[0])
