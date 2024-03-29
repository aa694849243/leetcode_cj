'''给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

示例 1:

输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
示例 2:

输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
注意:

0 < s1.length, s2.length <= 1000。
所有字符串中的字符ASCII值在[97, 122]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 动态规划中当前情况只需要考虑之前一步的情况，如果两个字符相同，那么当前最优的情况就是不删除任何字符。
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[float('inf')] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(len(s2), -1, -1):
            if i == len(s2):
                dp[-1][i] = 0
            else:
                dp[-1][i] = dp[-1][i + 1] + ord(s2[i])
        for j in range(len(s1), -1, -1):
            if j == len(s1):
                dp[j][-1] = 0
            else:
                dp[j][-1] = dp[j + 1][-1] + ord(s1[j])
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i][j + 1] + ord(s2[j]), dp[i + 1][j] + ord(s1[i]))
        return dp[0][0]


Solution().minimumDeleteSum("deleat", "leet")
