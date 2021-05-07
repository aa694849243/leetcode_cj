# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
#
#
#
#
#
#  示例 1：
#
#  输入："ab-cd"
# 输出："dc-ba"
#
#
#  示例 2：
#
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
#
#  示例 3：
#
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
#
#
#
#  提示：
#
#
#  S.length <= 100
#  33 <= S[i].ASCIIcode <= 122
#  S 中不包含 \ or "
#
#  Related Topics 字符串
#  👍 80 👎 0


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        l, r = 0, len(s)-1
        while l < r:
            while l < len(s) and not s[l].isalpha():
                l += 1
            while r >= 0 and not s[r].isalpha():
                r -= 1
            if not l < r:
                break
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
Solution().reverseOnlyLetters("ab-cd")