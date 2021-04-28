# 求出大于或等于 N 的最小回文素数。
#
#  回顾一下，如果一个数大于 1，且其因数只有 1 和它自身，那么这个数是素数。
#
#  例如，2，3，5，7，11 以及 13 是素数。
#
#  回顾一下，如果一个数从左往右读与从右往左读是一样的，那么这个数是回文数。
#
#  例如，12321 是回文数。
#
#
#
#  示例 1：
#
#  输入：6
# 输出：7
#
#
#  示例 2：
#
#  输入：8
# 输出：11
#
#
#  示例 3：
#
#  输入：13
# 输出：101
#
#
#
#  提示：
#
#
#  1 <= N <= 10^8
#  答案肯定存在，且小于 2 * 10^8。
#
#
#
#
#
#  Related Topics 数学
#  👍 64 👎 0

# 素数类问题
class Solution:
    def primePalindrome(self, N: int) -> int:
        def isprime(n):
            return n > 1 and all(n % d for d in range(2,int(n ** .5) + 1))
        if 7<N<=11:
            return 11
        for length in range(1, 6):  # 只用考虑奇数
            for num in range(10 ** (length - 1), 10 ** length):
                a = str(num)
                b = int(a + a[-2::-1])  # 只考虑奇数
                if b < N:
                    continue
                if isprime(b):
                    return b
Solution().primePalindrome(6)