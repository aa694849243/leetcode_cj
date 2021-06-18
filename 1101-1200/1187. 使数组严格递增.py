# -*- coding: utf-8 -*-
import bisect
from typing import List


# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
#
#  每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j
# < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
#
#  如果无法让 arr1 严格递增，请返回 -1。
#
#
#
#  示例 1：
#
#  输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# 输出：1
# 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
#
#
#  示例 2：
#
#  输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# 输出：2
# 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
#
#
#  示例 3：
#
#  输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# 输出：-1
# 解释：无法使 arr1 严格递增。
#
#
#
#  提示：
#
#
#  1 <= arr1.length, arr2.length <= 2000
#  0 <= arr1[i], arr2[i] <= 10^9
#
#
#
#  Related Topics 动态规划
#  👍 62 👎 0
# https://leetcode-cn.com/problems/make-array-strictly-increasing/solution/yi-wei-dp-si-lu-xiang-jie-cpy3-by-newhar/
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        arr1 = [-1] + arr1 + [float('inf')]  # 加哨兵
        dp = [float('inf')] * (n := len(arr1))
        dp[0] = 0
        for i in range(1, n):
            j = bisect.bisect_left(arr2, arr1[i])  # j代表arr2中可以替换的个数
            for k in range(1, min(j, i - 1) + 1):
                if arr1[i - k - 1] < arr2[j - k]:
                    dp[i] = min(dp[i], dp[i - k - 1] + k)
            if arr1[i - 1] < arr1[i]:
                dp[i] = min(dp[i - 1], dp[i])
        return dp[-1] if dp[-1]!=float('inf') else -1
