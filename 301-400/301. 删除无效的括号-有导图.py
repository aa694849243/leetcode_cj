'''删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 回溯法
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        mleft = mright = 0
        for i in s:
            if i == '(':
                mleft += 1
            elif i == ')' and mleft > 0:
                mleft -= 1
            elif i == ')':
                mright += 1
        n = len(s)
        res = set()

        def backtrack(s, index, left_num, right_num, misleft, misright, expr):
            if index == n:
                if misleft == mleft and misright == mright:
                    res.add(''.join(expr))
            elif misleft <= mleft and misright <= mright:
                if s[index] not in ('(', ')'):
                    expr.append(s[index])
                    backtrack(s, index + 1, left_num, right_num, misleft, misright, expr)
                    expr.pop()
                else:
                    backtrack(s, index + 1, left_num, right_num, misleft + int(s[index] == '('),
                              misright + int(s[index] == ')'), expr)
                    if s[index] == '(':
                        expr.append(s[index])
                        backtrack(s, index + 1, left_num + 1, right_num, misleft, misright, expr)
                        expr.pop()
                    elif s[index] == ')' and left_num > right_num:
                        expr.append(s[index])
                        backtrack(s, index + 1, left_num, right_num + 1, misleft, misright, expr)
                        expr.pop()

        backtrack(s, 0, 0, 0, 0, 0, [])
        return list(res)

Solution().removeInvalidParentheses(")(")