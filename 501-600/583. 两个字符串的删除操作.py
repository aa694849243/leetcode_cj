'''给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

 

示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
 

提示：

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1记忆化递归
# 找公共子串
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = {}

        def rec(s1, s2, i, j):
            if (i, j) in m:
                return m[(i, j)]
            if i < 0 or j < 0:
                return 0
            if s1[i] == s2[j]:
                ans = 1 + rec(s1, s2, i - 1, j - 1)

            else:
                ans = max(rec(s1, s2, i - 1, j), rec(s1, s2, i, j - 1))
            m[(i, j)] = ans
            return ans

        lcs = rec(word1, word2, len(word1) - 1, len(word2) - 1)
        return len(word1) + len(word2) - 2 * lcs


# 2动态规划
# 公共子串lcs
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (1 + len(word2)) for _ in range(1 + len(word1))]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


# 3动态规划
# 不求公共子串lcs
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # dp[i][j]代表s1[:i+1]和s2[:j+1]最少需要删除多少个字符
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for i in range(1, len(word2) + 1):
            dp[0][i] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[-1][-1]


# 4动态规划
# 一维数组
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [i for i in range(len(word2) + 1)]
        for i in range(1,len(word1)+1):
            tmp = [i]
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    tmp.append(dp[j-1])
                else:
                    tmp.append(min(tmp[-1],dp[j])+1)
            dp=tmp
        return dp[-1]


Solution().minDistance("ss", "e")
