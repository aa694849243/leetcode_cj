#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配
# 是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
#
#  示例 1:
#
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
#
#  示例 2:
#
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
#  示例 3:
#
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#  示例 4:
#
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#
#  示例 5:
#
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#
#
#  s 可能为空，且只包含从 a-z 的小写字母。
#  p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
#
#
#  注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/
#
#  Related Topics 递归 字符串 动态规划
#  👍 254 👎 0


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s  # p为空时，s为空才匹配
        first_match = len(s) > 0 and p[0] in ('.', s[0])
        if len(p) >= 2 and p[1] == '*':  # 遇到‘*’号时处理方式
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))  # p[2]及其之后的继续比对，如果第一个对上了，则将s[0]删掉，继续比对
        else:
            return first_match and self.isMatch(s[1:], p[1:])


# 复写

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(m)] for _ in range(n)]
        dp[-1][-1] = True
        for i in range(n - 1, -1, -1):
            for j in range(m - 2, -1, -1):
                first_match = i < len(s) and p[j] in ('.', s[i])
                if j < len(p) - 1 and p[j + 1] == '*':
                    dp[i][j]=dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j]=first_match and dp[i+1][j+1]
        return dp[0][0]




Solution().isMatch("ab", ".*c")
