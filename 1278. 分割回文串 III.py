# -*- coding: utf-8 -*-


# 给你一个由小写字母组成的字符串 s，和一个整数 k。
#
#  请你按下面的要求分割字符串：
#
#
#  首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
#  接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
#
#
#  请返回以这种方式分割字符串所需修改的最少字符数。
#
#
#
#  示例 1：
#
#  输入：s = "abc", k = 2
# 输出：1
# 解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
#
#
#  示例 2：
#
#  输入：s = "aabbc", k = 3
# 输出：0
# 解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。
#
#  示例 3：
#
#  输入：s = "leetcode", k = 8
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= k <= s.length <= 100
#  s 中只含有小写英文字母。
#
#  Related Topics 动态规划
#  👍 77 👎 0


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for leng in range(2, n + 1):
            for l in range(n - leng + 1):
                r = l + leng - 1
                if l+1<=r-1:
                    cost[l][r] = cost[l + 1][r - 1] + (0 if s[l] == s[r] else 1)
                else:
                    cost[l][r]=0 if s[l]==s[r] else 1
        f = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    f[i][j] = cost[0][i - 1]
                else:
                    for i0 in range(j - 1, i):  # i0>=j-1,cost[i0]代表真正的i0，而f[i0]为i0-1
                        f[i][j] = min(f[i][j], f[i0][j - 1] + cost[i0][i - 1])
        return f[-1][-1]
Solution().palindromePartition('abc',2)