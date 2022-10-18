# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-09-21 2:23 
# ide： PyCharm
# 你写下了若干 正整数 ，并将它们连接成了一个字符串 num 。但是你忘记给这些数字之间加逗号了。你只记得这一列数字是 非递减 的且 没有 任何数字有前导 0
#  。
#
#  请你返回有多少种可能的 正整数数组 可以得到字符串 num 。由于答案可能很大，将结果对 10⁹ + 7 取余 后返回。
#
#
#
#  示例 1：
#
#  输入：num = "327"
# 输出：2
# 解释：以下为可能的方案：
# 3, 27
# 327
#
#
#  示例 2：
#
#  输入：num = "094"
# 输出：0
# 解释：不能有数字有前导 0 ，且所有数字均为正数。
#
#
#  示例 3：
#
#  输入：num = "0"
# 输出：0
# 解释：不能有数字有前导 0 ，且所有数字均为正数。
#
#
#  示例 4：
#
#  输入：num = "9999999999999"
# 输出：101
#
#
#
#
#  提示：
#
#
#  1 <= num.length <= 3500
#  num 只含有数字 '0' 到 '9' 。
#
#
#  Related Topics 字符串 动态规划 后缀数组 👍 28 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
#一维数组最长公共前缀 一维lcp
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        mod = 10 ** 9 + 7
        n = len(num)
        if num[0] == "0":
            return 0
        lcp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):  # 最长公共前缀
            lcp[i][n - 1] = +(num[i] == num[n - 1])
            for j in range(i + 1, n - 1):
                lcp[i][j] = lcp[i + 1][j + 1] + 1 if num[i] == num[j] else 0
        lcp[-1][-1] = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, n):
            if num[i] == '0':
                continue
            presum = 0
            for j in range(i,n):
                dp[i][j] = presum % mod
                length = j - i + 1
                if i - length >= 0:
                    if lcp[i - length][i] >= length or num[i + lcp[i - length][i]] > num[i - length + lcp[i - length][i]]:
                        dp[i][j] += dp[i - length][i - 1]
                        dp[i][j] %= mod
                    presum += dp[i - length][i - 1]
        return sum(dp[i][-1] for i in range(n)) %mod
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numberOfCombinations("1203"))