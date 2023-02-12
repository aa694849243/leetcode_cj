# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-24 23:04 
# ide： PyCharm
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k==1:
            return n
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        f = [0] * n
        for i in range(n):
            for j in range(0, i):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 >= k:
                        if j == 0:
                            f[i] = max(f[i], 1)
                        else:
                            f[i] = max(f[i], f[j - 1] + 1)
            f[i] = max(f[i], f[i - 1])
        return f[-1]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxPalindromes(
    "iqqibcecvrbxxj",
    1
))

