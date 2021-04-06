'''
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

 

示例 1：

输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2：

输入：S = "babgbag", T = "bag"
输出：5
解释：

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s:
            return int(not t)
        if not t:
            return 1
        dp = [[0] * len(s) for _ in range(len(t))]
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, len(s)):
            dp[0][i] = dp[0][i - 1] + 1 if s[i] == t[0] else dp[0][i - 1]
        for i in range(1, len(t)):
            for j in range(1, len(s)):
                if s[j] != t[i]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j-1]
        return dp[-1][-1]


S = "rabbbit"
T = "rabbit"
Solution().numDistinct(S, T)
