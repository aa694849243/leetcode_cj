# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-20 21:49 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [''] * n
        i = 0
        for ch in ascii_lowercase:
            while i < n and s[i]:
                i += 1
            if i == n:
                break
            for j in range(i, n):
                if lcp[i][j]:
                    s[j] = ch
        if '' in s:
            return ''
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1 if i != n - 1 and j != n - 1 else 1
                if dp[i][j] != lcp[i][j]:
                    return ''
        return ''.join(s)
# leetcode submit region end(Prohibit modification and deletion)

