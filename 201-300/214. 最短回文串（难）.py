'''
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 双指针 递归
# 分析见题解 https://leetcode-cn.com/problems/shortest-palindrome/solution/zui-duan-hui-wen-chuan-by-leetcode/
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        def rec(s):
            left, right = 0, len(s) - 1
            while right > -1:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    right -= 1
            if left == len(s):
                return s
            else:
                return s[left:][::-1] + rec(s[:left]) + s[left:]

        return rec(s)


# KMP
# pnext中每个位置数值为该位置之前（不包括该位置）的首尾相同字符串长度
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        s = s + '#' + s[::-1] + '$'  # +'#'为了防止混淆字符串比如‘aaaaa’这样的，结果会是9，实际应该是5
        pnext = [-1] * len(s)
        k, i = -1, 0
        while i < len(s) - 1:
            if s[i] == s[k] or k == -1:
                k += 1
                i += 1
                pnext[i] = k
            else:
                k = pnext[k]
        s=s[:n]
        lenth=pnext[-1]
        return s[lenth:][::-1]+s[:lenth]+s[lenth:]


a = "aaaaa"
Solution().shortestPalindrome(a)
