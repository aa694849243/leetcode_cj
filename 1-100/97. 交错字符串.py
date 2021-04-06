'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 回溯法，超时
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(s1, s2, s3):
            if not s1 and not s2 and not s3:
                return True
            elif not s3:
                return False
            elif not s1:
                return s2 == s3
            elif not s2:
                return s1 == s3
            if s3[0] != s1[0] and s3[0] != s2[0]:
                return False
            elif s3[0] == s1[0] and s3[0] != s2[0]:
                return dfs(s1[1:], s2, s3[1:])
            elif s3[0] == s2[0] and s3[0] != s1[0]:
                return dfs(s1, s2[1:], s3[1:])
            else:
                if dfs(s1[1:], s2, s3[1:]):
                    return True
                else:
                    return dfs(s1, s2[1:], s3[1:])

        return dfs(s1, s2, s3)


# 简洁的回溯法
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not len(s1) + len(s2) == len(s3): return False

        def restore(s1, s2, s3):
            if s3 == '':
                return True

            r1, r2 = False, False
            if s1 and s3[0] == s1[0]:
                r1 = restore(s1[1:], s2, s3[1:])

            if s2 and s3[0] == s2[0]:
                r2 = restore(s1, s2[1:], s3[1:])

            return r1 or r2

        return restore(s1, s2, s3)

# 三维动态规划 6%
class Solution:
    def isinterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1 + s2) != len(s3):
            return False

        dp = [[[False] * (len(s1) + 1) for _ in range(len(s2) + 1)] for _ in range(len(s3) + 1)]
        for j in range(len(s1) + 1):
            for k in range(len(s2) + 1):
                dp[0][k][j] = True
        for i in range(1, len(s3) + 1):
            for j in range(len(s1) + 1):
                if i < j:
                    continue
                for k in range(len(s2) + 1):
                    if i != k + j:
                        continue
                    else:
                        if k - 1 >= 0 and s3[i - 1] == s2[k - 1]:
                            dp[i][k][j] = dp[i - 1][k - 1][j]
                        if j - 1 >= 0 and s3[i - 1] == s1[j - 1]:
                            if not dp[i][k][j]:
                                dp[i][k][j] = dp[i - 1][k][j - 1]

        return dp[-1][-1][-1]


# 特殊二维动态规划
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and dp[j][i - 1] == True:
                    dp[j][i] = True
                if j > 0 and s2[j - 1] == s3[i + j - 1] and dp[j - 1][i] == True:
                    dp[j][i] = True
        return dp[-1][-1]


# 特殊一维动态规划 滚动数组 dp为滚动的纵轴
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if j == 0 and i == 0:
                    dp[0] = True
                elif j > 0 and s2[j - 1] == s3[i + j - 1] and dp[j - 1]:
                    dp[j] = True
                elif i > 0 and s1[i - 1] == s3[i + j - 1] and dp[j]:
                    dp[j] = True
                else:
                    dp[j] = False
        return dp[-1]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

Solution().isInterleave(s1, s2, s3)
