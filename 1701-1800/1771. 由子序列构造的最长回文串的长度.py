# -*- coding: utf-8 -*-
# 给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串：
#
#
#  从 word1 中选出某个 非空 子序列 subsequence1 。
#  从 word2 中选出某个 非空 子序列 subsequence2 。
#  连接两个子序列 subsequence1 + subsequence2 ，得到字符串。
#
#
#  返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。
#
#  字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。
#
#  回文串 是正着读和反着读结果一致的字符串。
#
#
#
#  示例 1：
#
#  输入：word1 = "cacb", word2 = "cbba"
# 输出：5
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。
#
#  示例 2：
#
#  输入：word1 = "ab", word2 = "ab"
# 输出：3
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。
#
#  示例 3：
#
#  输入：word1 = "aa", word2 = "bb"
# 输出：0
# 解释：无法按题面所述方法构造回文串，所以返回 0 。
#
#
#
#  提示：
#
#
#  1 <= word1.length, word2.length <= 1000
#  word1 和 word2 由小写英文字母组成
#
#
#  Related Topics 字符串 动态规划 👍 45 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        if not (set(word1) & set(word2)):
            return 0
        l, r = len(word1), len(word2)
        s = word1 + word2
        ans = float('-inf')
        dp = [[1] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        if i + 1 <= j - 1:
                            dp[i][j] = dp[i + 1][j - 1] + 2
                        else:
                            dp[i][j] = 2
                        if i < l and j >= l:
                            ans = max(dp[i][j], ans)
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
# author： caoji
# datetime： 2022-08-24 23:30 
# ide： PyCharm