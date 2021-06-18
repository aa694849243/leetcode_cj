# -*- coding: utf-8 -*-
import itertools
from typing import List


# 给你一个整数数组 arr 和一个整数 k。
#
#  首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。
#
#
#  举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。
#
#
#  然后，请你返回修改后的数组中的最大的子数组之和。
#
#  注意，子数组长度可以是 0，在这种情况下它的总和也是 0。
#
#  由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。
#
#
#
#  示例 1：
#
#  输入：arr = [1,2], k = 3
# 输出：9
#
#
#  示例 2：
#
#  输入：arr = [1,-2,1], k = 5
# 输出：2
#
#
#  示例 3：
#
#  输入：arr = [-1,-2], k = 7
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 10^5
#  1 <= k <= 10^5
#  -10^4 <= arr[i] <= 10^4
#
#  Related Topics 动态规划
#  👍 75 👎 0


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        a = sum(arr)
        ans = max(0, a)
        mod = 10 ** 9 + 7

        def kadane(arr):
            ans = float('-inf')
            cur = 0
            for x in arr:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        k1 = kadane(arr)
        maxleft = max([0] + [*itertools.accumulate(arr)])
        maxright = max([0] + [*itertools.accumulate(arr[::-1])])
        if a > 0:
            ans = max(a * k, ans)
            ans = max(k1, a * (k - 2) + maxleft + maxright, ans) % mod
        else:
            ans = max(k1, maxleft + maxright, ans) % mod
        return ans if k >= 2 else max(k1, 0) % mod
