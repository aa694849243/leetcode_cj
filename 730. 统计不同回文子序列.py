'''给定一个字符串 S，找出 S 中不同的非空回文子序列个数，并返回该数字与 10^9 + 7 的模。

通过从 S 中删除 0 个或多个字符来获得子序列。

如果一个字符序列与它反转后的字符序列一致，那么它是回文字符序列。

如果对于某个  i，A_i != B_i，那么 A_1, A_2, ... 和 B_1, B_2, ... 这两个字符序列是不同的。

 

示例 1：

输入：
S = 'bccb'
输出：6
解释：
6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
示例 2：

输入：
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：
共有 3104860382 个不同的非空回文子序列，对 10^9 + 7 取模为 104860361。
 

提示：

字符串 S 的长度将在[1, 1000]范围内。
每个字符 S[i] 将会是集合 {'a', 'b', 'c', 'd'} 中的某一个

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-different-palindromic-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1官方
class Solution(object):
    def countPalindromicSubsequences(self, S):
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        prv = [-1] * N
        nxt = [-1] * N

        last = [-1] * 4
        for i in range(N):
            last[A[i]] = i
            prv[i] = tuple(last)

        last = [-1] * 4
        for i in range(N - 1, -1, -1):
            last[A[i]] = i
            nxt[i] = tuple(last)

        MOD = 10 ** 9 + 7
        memo = [[None] * N for _ in range(N)]

        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1
            if i <= j:
                for x in range(4):
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    if i <= i0 <= j:
                        ans += 1
                    if -1 < i0 < j0:
                        ans += dp(i0 + 1, j0 - 1)
            ans %= MOD
            memo[i][j] = ans
            return ans

        return dp(0, N - 1) - 1


# 2特殊动态规划 三维动态规划
class Solution(object):
    def countPalindromicSubsequences(self, S):
        dp = [[[0] * 4 for _ in range(len(S))] for _ in range(len(S))]
        mod = 10 ** 9 + 7
        s = [ord(c) - ord('a') for c in S]
        for i in range(len(S) - 1, -1, -1):
            for j in range(i, len(S)):
                for k in range(4):
                    if i == j:
                        dp[i][j][k] = 1 if s[i] == k else 0
                    else:
                        if s[i] != k:
                            dp[i][j][k] = dp[i + 1][j][k]
                        elif s[j] != k:
                            dp[i][j][k] = dp[i][j - 1][k]
                        else:  # s[i]=s[j]=k
                            if i + 1 > j - 1:
                                dp[i][j][k] = 2
                            else:
                                dp[i][j][k] = (2 + sum(dp[i + 1][j - 1][n] for n in range(4))) % mod

        return sum(dp[0][-1][i] for i in range(4)) % mod


# 3递归 前一个a后一个a
class Solution(object):
    def countPalindromicSubsequences(self, S):
        mod = 10 ** 9 + 7
        s = [ord(c) - ord('a') for c in S]
        prev = [None for _ in range(len(S))]
        nxt = [None for _ in range(len(S))]
        last = [-1, -1, -1, -1]
        for i in range(len(s)):
            last[s[i]] = i
            prev[i] = tuple(last)
        last = [-1, -1, -1, -1]
        for i in range(len(s) - 1, -1, -1):
            last[s[i]] = i
            nxt[i] = tuple(last)
        m = {}

        def rec(i, j):
            if (i, j) in m:
                return m[(i, j)]
            if i == j:
                return 1
            if i > j:
                return 0
            ans = 0
            for x in range(4):
                i0 = nxt[i][x]
                j0 = prev[j][x]
                if i <= i0 == j0 <= j:
                    ans += 1
                if i <= i0 < j0 <= j:
                    ans += (2 + rec(i0 + 1, j0 - 1)) % mod
            m[(i, j)] = ans % mod
            return ans % mod

        return rec(0, len(s) - 1)


Solution().countPalindromicSubsequences("baac")
