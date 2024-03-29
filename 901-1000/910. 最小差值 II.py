# 给你一个整数数组 A，对于每个整数 A[i]，可以选择 x = -K 或是 x = K （K 总是非负整数），并将 x 加到 A[i] 中。
#
#  在此过程之后，得到数组 B。
#
#  返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
#
#
#  示例 2：
#
#
# 输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
#
#
#  示例 3：
#
#
# 输入：A = [1,3,6], K = 3
# 输出：3
# 解释：B = [4,6,3]
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 10000
#  0 <= A[i] <= 10000
#  0 <= K <= 10000
#
#  Related Topics 贪心算法 数学
#  👍 102 👎 0

from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        ma = max(A)
        mi = min(A)
        A.sort()
        ans = ma - mi
        for i in range(len(A) - 1):  # 找+K，-K的分界点
            a, b = A[i], A[i + 1]  # 如果a+K，b-K是分界点，(mi+k,b-k)都有可能是最低点，(a+k,ma-k)都有可能是最高点
            ans = min(ans, max(a + K, ma - K) - min(mi + K, b - K))
        return ans
