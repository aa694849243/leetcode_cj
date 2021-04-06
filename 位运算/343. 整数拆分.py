'''给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 数学 O(n)解法
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        dp = [0] * (n + 1)
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n + 1):
            dp[i] = max(2 * (i - 2), 3 * (i - 3), 2 * dp[i - 2], 3 * dp[i - 3])
        return dp[-1]


# 数学 O(1)解法
class Solution:
    def integerBreak(self, n: int) -> int:
        if n<4:
            return n-1
        exponent, reminder = n // 3, n % 3
        if reminder==0:
            return 3**exponent
        elif reminder==1:
            return 3**(exponent-1)*2*2
        elif reminder==2:
            return 3**exponent*2