'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 回溯法，时间超出限制------------------------------------------------------------------------
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s:
            return not p.strip('*')
        if not p:
            return not s
        firstmatch = len(s) > 0 and p[0] in (s[0], '*', "?")
        if len(p) > 0 and p[0] == '*':
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        else:
            return firstmatch and self.isMatch(s[1:], p[1:])


# 动态规划-----------caojie-15%-----------------------------------------------------------------------------------------------
#解题思路https://leetcode-cn.com/problems/wildcard-matching/solution/zi-di-xiang-shang-dong-tai-gui-hua-by-aa694849243/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s:
            return not p.strip('*')
        if not p:
            return not s
        ans = [[False] * len(p) for _ in range(len(s))]
        if p[0] in (s[0], '?', '*'):
            ans[0][0] = True
        for j in range(len(p)):
            for i in range(len(s)):
                firstmatch = p[j] in (s[i], '*', "?")
                if p[j] == '*':
                    if j - 1 >= 0 and i - 1 >= 0:
                        ans[i][j] = ans[i][j - 1] or ans[i - 1][j]
                    elif j - 1 >= 0 and i - 1 < 0:
                        ans[i][j] = (not p[:j + 1].strip('*')) or p[:j + 1].strip('*') in (s[i], '?')
                    elif i - 1 >= 0 and j - 1 < 0:
                        ans[i][j] = True
                else:
                    if j - 1 >= 0 and i - 1 >= 0:
                        ans[i][j] = firstmatch and ans[i - 1][j - 1]
                    elif j - 1 >= 0 and i - 1 < 0:
                        ans[i][j] = not p[:j].lstrip('*') and firstmatch
                    elif i - 1 >= 0 and j - 1 < 0:
                        ans[i][j] = False
        return ans[i][j]


s = "mississippi"
p = "m??*"
Solution().isMatch(s, p)
