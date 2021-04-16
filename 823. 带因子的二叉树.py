# 给出一个含有不重复整数元素的数组，每个整数均大于 1。
#
#  我们用这些整数来构建二叉树，每个整数可以使用任意次数。
#
#  其中：每个非叶结点的值应等于它的两个子结点的值的乘积。
#
#  满足条件的二叉树一共有多少个？返回的结果应模除 10 ** 9 + 7。
#
#
#
#  示例 1:
#
#
# 输入: A = [2, 4]
# 输出: 3
# 解释: 我们可以得到这些二叉树: [2], [4], [4, 2, 2]
#
#  示例 2:
#
#
# 输入: A = [2, 4, 5, 10]
# 输出: 7
# 解释: 我们可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
#
#
#
#  提示:
#
#
#  1 <= A.length <= 1000.
#  2 <= A[i] <= 10 ^ 9.
#
#  👍 53 👎 0
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = max(arr)
        m = set(arr)
        dp = collections.defaultdict(int)
        arr.sort()
        mod = 10 ** 9 + 7
        for i, num in enumerate(arr):
            dp[num] += 1
            if num ** 2 in m:
                dp[num ** 2] += dp[num] * dp[num] % mod
            for j in range(i):
                if num * arr[j] in m:
                    dp[num * arr[j]] += 2 * dp[num] * dp[arr[j]] % mod
        return sum(dp.values()) % mod
Solution().numFactoredBinaryTrees([40,10,8,4,5])
