# 给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?
#
#  示例 1:
#
#
# 输入: 5
# 输出: 2
# 解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
#
#  示例 2:
#
#
# 输入: 9
# 输出: 3
# 解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
#
#  示例 3:
#
#
# 输入: 15
# 输出: 4
# 解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
#
#  说明: 1 <= N <= 10 ^ 9
#  Related Topics 数学
#  👍 100 👎 0


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        while N & 1 == 0:
            N >>= 1
        ans = 1
        d = 3
        while d * d < N:
            e = 0
            if N % d == 0:
                N //= d
                e += 1
            ans *= e + 1
        if N > 1:
            ans *= 2
        return ans
