'''给定一个字符串 S，计算 S 的不同非空子序列的个数。

因为结果可能很大，所以返回答案模 10^9 + 7.

 

示例 1：

输入："abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
示例 2：

输入："aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
示例 3：

输入："aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
 

 

提示：

S 只包含小写字母。
1 <= S.length <= 2000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1递归 2x+1法
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        mod = 10 ** 9 + 7
        s = [ord(c) - ord('a') for c in S]
        prev = [None] * len(s)
        last = [-1] * 26
        for i in range(len(s)):
            last[s[i]] = i
            prev[i] = tuple(last)
        m = {}

        def rec(j):
            if j in m:
                return m[j]
            if j == -1:
                return 0
            if j == 0:
                return 1
            x = prev[j - 1][s[j]]
            if x == -1:
                ans = 2 * rec(j - 1) + 1
            else:
                ans = 2 * rec(j - 1) + 1 - rec(x - 1) - 1  # rec(x-1)+1为重复的数 比如 abcdb最后一个以b结尾的数要减去前面那个以b结尾的数
            m[j] = ans % mod
            return ans % mod

        return rec(len(S) - 1)


# 2递归 2x法
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        mod = 10 ** 9 + 7
        s = [ord(c) - ord('a') for c in S]
        prev = [None] * len(s)
        last = [-1] * 26
        for i in range(len(s)):
            last[s[i]] = i
            prev[i] = tuple(last)
        m = {}

        def rec(j):
            if j in m:
                return m[j]
            if j == -1:
                return 1
            if j == 0:
                return 2
            x = prev[j - 1][s[j]]
            if x == -1:
                ans = 2 * rec(j - 1)
            else:
                ans = 2 * rec(j - 1) - rec(x - 1)
            m[j] = ans % mod
            return ans % mod

        return rec(len(S) - 1) - 1


# 3动态规划
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        dp = [1]
        m = {}
        for i, s in enumerate(S):
            dp.append(dp[-1] * 2)
            if s in m:
                dp[-1]-=dp[m[s]]
            m[s]=i
        return (dp[-1]-1) % (10**9+7)

Solution().distinctSubseqII('aaa')
