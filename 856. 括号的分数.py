# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
#
#  () 得 1 分。
#  AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
#  (A) 得 2 * A 分，其中 A 是平衡括号字符串。
#
#
#
#
#  示例 1：
#
#  输入： "()"
# 输出： 1
#
#
#  示例 2：
#
#  输入： "(())"
# 输出： 2
#
#
#  示例 3：
#
#  输入： "()()"
# 输出： 2
#
#
#  示例 4：
#
#  输入： "(()(()))"
# 输出： 6
#
#
#
#
#  提示：
#
#
#  S 是平衡括号字符串，且只含有 ( 和 ) 。
#  2 <= S.length <= 50
#
#  Related Topics 栈 字符串
#  👍 202 👎 0


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def cal(s):
            if len(s) == 2: return 1
            bal = 0
            score = 0
            flag = 0
            for i, ch in enumerate(s):
                if ch == ')':
                    bal -= 1
                else:
                    bal += 1
                if bal == 0:
                    if len(s[flag:i + 1]) == 2:
                        score += 1
                    else:
                        score += 2 * cal(s[flag + 1:i])
                    flag = i + 1
            return score
        return cal(S)
Solution().scoreOfParentheses('()()')