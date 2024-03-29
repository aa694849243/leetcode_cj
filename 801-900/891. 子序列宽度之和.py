# 给定一个整数数组 A ，考虑 A 的所有非空子序列。
#
#  对于任意序列 S ，设 S 的宽度是 S 的最大元素和最小元素的差。
#
#  返回 A 的所有子序列的宽度之和。
#
#  由于答案可能非常大，请返回答案模 10^9+7。
#
#
#
#  示例：
#
#  输入：[2,1,3]
# 输出：6
# 解释：
# 子序列为 [1]，[2]，[3]，[2,1]，[2,3]，[1,3]，[2,1,3] 。
# 相应的宽度是 0，0，0，1，1，2，2 。
# 这些宽度之和是 6 。
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 20000
#  1 <= A[i] <= 20000
#
#  Related Topics 数组 数学
#  👍 44 👎 0


from typing import List


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        mod = 10 ** 9 + 7
        pow2 = [1]
        n = len(A)
        for i in range(n - 1):
            pow2.append(pow2[-1] * 2 % mod)  # %优先级比较低
        ans = 0
        for i in range(n):
            ans += (pow2[i] - pow2[n - i - 1]) * A[i]
            ans %= mod
        return ans
Solution().sumSubseqWidths([2,1,3])