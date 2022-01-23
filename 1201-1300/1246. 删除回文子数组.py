# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。
#
#
#  注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。
#
#  请你计算并返回从数组中删除所有数字所需的最少操作次数。
#
#
#
#  示例 1：
#
#  输入：arr = [1,2]
# 输出：2
#
#
#  示例 2：
#
#  输入：arr = [1,3,4,1,5]
# 输出：3
# 解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 100
#  1 <= arr[i] <= 20
#
#  Related Topics 数组 动态规划 👍 63 👎 0


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        dp = [[float('inf')] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            for j in range(i, len(arr)):
                if i == j:
                    dp[i][j] = 1
                elif j - i == 1:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    dp[i][j] = dp[i + 1][j] + 1
                    for k in range(i, j + 1):
                        if i == k:
                            dp[i][j] = min(dp[i][j], dp[k + 1][j] + 1)
                        elif arr[i] == arr[k]:
                            if i + 1 == k:
                                tmp = dp[k + 1][j] + 1 if k + 1 <= j else 1
                            else:
                                tmp = dp[i + 1][k - 1] + dp[k + 1][j] if k + 1 <= j else dp[i + 1][k - 1]
                            dp[i][j] = min(tmp, dp[i][j])
        return dp[0][len(arr) - 1]


Solution().minimumMoves([1, 2])
