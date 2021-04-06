'''给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1 普通方法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = lt = 0
        while ls < len(s) and lt < len(t):
            if s[ls] == t[lt]:
                ls += 1
                lt += 1
            else:
                lt += 1
        return ls == len(s)


# 2 动态规划
# 构建dp阶段 从前往后找 转移方程为为dp[i][j]=dp[i+1][j] or i，如果当前位置为目标匹配字母则该位置值为当前位置，其他字母的位置为序列中当前字母之后的对应字母位置，找不到设置值为m
# 匹配序列阶段 从子序列出发，每次更新下一次需要在主序列什么位置开始找
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            return not s
        m = len(t)
        dp = [[m] * 26 for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(26):
                dp[i][j] = dp[i + 1][j] if j != ord(t[i]) - 97 else i
        add = 0
        j = 0
        while j < len(s):
            if dp[add][ord(s[j]) - 97] == m:
                return False
            add = dp[add][ord(s[j]) - 97] + 1
            j += 1
        return True


a = "acb"
b="ahbgdc"
Solution().isSubsequence(a, b)
