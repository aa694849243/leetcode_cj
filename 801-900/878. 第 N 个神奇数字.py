# 如果正整数可以被 A 或 B 整除，那么它是神奇的。
#
#  返回第 N 个神奇数字。由于答案可能非常大，返回它模 10^9 + 7 的结果。
#
#
#
#
#
#
#  示例 1：
#
#  输入：N = 1, A = 2, B = 3
# 输出：2
#
#
#  示例 2：
#
#  输入：N = 4, A = 2, B = 3
# 输出：6
#
#
#  示例 3：
#
#  输入：N = 5, A = 2, B = 4
# 输出：10
#
#
#  示例 4：
#
#  输入：N = 3, A = 6, B = 4
# 输出：8
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#  2 <= A <= 40000
#  2 <= B <= 40000
#
#  Related Topics 数学 二分查找
#  👍 75 👎 0


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        l = a * b // math.gcd(a, b)
        m = l // a + l // b - 1
        q, r = n // m, n % m
        ans = l * q
        MOD = 10 ** 9 + 7
        if r == 0:
            return ans % MOD
        head = [a, b]
        for i in range(r - 1):
            if head[0] <= head[1]:
                head[0] += a
            else:
                head[1] += b
        return (ans + min(head)) % MOD


# 2二分
# 上界为4*10^4*10^9
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        mod = 10 ** 9 + 7
        L = a * b // math.gcd(a, b)

        def cal(n):
            return n // a + n // b - n // L

        l, r = 2, 10 ** 15
        while l < r:
            mid = (l + r) // 2
            if cal(mid) < n:
                l = mid + 1
            else:
                r = mid
        return l % mod


Solution().nthMagicalNumber(4, 2, 3)
