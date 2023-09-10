# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。 
# 
#  返回所有可能的结果。答案可以按 任意顺序 返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ")("
# 输出：[""]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 25 
#  s 由小写英文字母以及括号 '(' 和 ')' 组成 
#  s 中至多含 20 个括号 
#  
# 
#  Related Topics 广度优先搜索 字符串 回溯 
#  👍 867 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        mis_left, mis_right = 0, 0
        for ch in s:
            if ch == '(':
                mis_left += 1
            elif ch == ')':
                if mis_left > 0:
                    mis_left -= 1
                else:
                    mis_right += 1
        res = set()

        def back_track(idx, bal, left_rem, right_rem, expr):
            if idx == len(s):
                if bal == 0 and left_rem == 0 and right_rem == 0:
                    res.add(expr)
                return
            if s[idx] == '(':
                back_track(idx + 1, bal + 1, left_rem, right_rem, expr + '(')
                if left_rem > 0:
                    back_track(idx + 1, bal, left_rem - 1, right_rem, expr)
            elif s[idx] == ')':
                if bal > 0:
                    back_track(idx + 1, bal - 1, left_rem, right_rem, expr + ')')
                if right_rem > 0:
                    back_track(idx + 1, bal, left_rem, right_rem - 1, expr)
            else:
                back_track(idx + 1, bal, left_rem, right_rem, expr + s[idx])
        back_track(0, 0, mis_left, mis_right, '')
        return list(res)

# leetcode submit region end(Prohibit modification and deletion)
