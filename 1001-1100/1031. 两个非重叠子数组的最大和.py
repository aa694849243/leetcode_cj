# -*- coding: utf-8 -*-
import itertools
from typing import List


# 给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。（这里需要澄清的是，长为 L 的子数组可以出现在长为 M
#  的子数组之前或之后。）
#
#  从形式上看，返回最大的 V，而 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... +
#  A[j+M-1]) 并满足下列条件之一：
#
#
#
#
#  0 <= i < i + L - 1 < j < j + M - 1 < A.length, 或
#  0 <= j < j + M - 1 < i < i + L - 1 < A.length.
#
#
#
#
#  示例 1：
#
#  输入：A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
#
#
#  示例 2：
#
#  输入：A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# 输出：29
# 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
#
#
#  示例 3：
#
#  输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
#
#
#
#  提示：
#
#
#  L >= 1
#  M >= 1
#  L + M <= A.length <= 1000
#  0 <= A[i] <= 1000
#
#  Related Topics 数组
#  👍 96 👎 0


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0] + [*itertools.accumulate(nums)]
        ans = 0
        a = sum(nums[:secondLen])
        ma = {secondLen - 1: a}
        for i in range(secondLen, len(nums)):
            ma[i] = max(ma[i - 1], prefix[i + 1] - prefix[i - secondLen + 1])
        b = sum(nums[-secondLen:])
        mb = {len(nums) - secondLen: b}
        for i in range(len(nums) - secondLen - 1, -1, -1):
            mb[i] = max(mb[i + 1], prefix[i + secondLen] - prefix[i])
        for i in range(firstLen - 1, len(nums)):
            s1 = prefix[i + 1] - prefix[i - firstLen + 1]
            s2 = ma[i - firstLen] if i - firstLen in ma else 0
            s3 = mb[i + 1] if i + 1 in mb else 0
            ans = max(ans, s1 + s2, s1 + s3)
        return ans


Solution().maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2)
