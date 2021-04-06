'''给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

 

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。

 

提示：

1 <= s.length <= 1000
s 只包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 马拉车模板
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s = '#' + '#'.join(list(s)) + '#'
        p = [0] * len(s)
        mx = 0
        id = 0  # mx串的中心
        lens = len(s)
        for i in range(len(s)):
            if mx > i:
                p[i] = min(mx - i, p[2 * id - i])
            else:
                p[i] = 1
            while i + p[i] < lens and i - p[i] >= 0 and s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                id, mx = i, i + p[i],
        i_res = p.index(max(p))
        s_res = s[i_res - (p[i_res] - 1):i_res + p[i_res]]
        return s_res.replace('#', ''), max(p) - 1


Solution().longestPalindromeSubseq('babad')

# 1解题
import collections


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        dp = [[1] * len(s) for _ in range(len(s))]
        ans = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[j] == s[i]:
                        if j - 1 >= i + 1:
                            dp[i][j] = dp[i + 1][j - 1] + 2
                        else:
                            dp[i][j] = 2
                        ans=max(dp[i][j],ans)
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return ans